data "google_project" "project" {
  project_id = var.project_id
}

resource "google_iam_workload_identity_pool" "gh_pool" {
  project                   = var.project_id
  workload_identity_pool_id = "github-pool"
}

resource "google_iam_workload_identity_pool_provider" "provider" {
  project                            = var.project_id
  workload_identity_pool_id          = google_iam_workload_identity_pool.gh_pool.workload_identity_pool_id
  workload_identity_pool_provider_id = "github-provider"
  attribute_mapping                  = {
    "google.subject" = "assertion.sub"
    "attribute.full" = "assertion.repository"
  }
  oidc {
    issuer_uri        = "https://token.actions.githubusercontent.com"
  }

  depends_on = [
    google_iam_workload_identity_pool.gh_pool
  ]
}

resource "google_service_account" "runner_sa" {
  project      = var.project_id
  account_id   = "github-runner"
  display_name = "Service Account"

  depends_on = [
    google_iam_workload_identity_pool.gh_pool
  ]
}

data "google_iam_policy" "wli_user_ghshr" {
  binding {
    role = "roles/iam.workloadIdentityUser"
    
    members = [
      "principalSet://iam.googleapis.com/projects/${data.google_project.project.number}/locations/global/workloadIdentityPools/github-pool/attribute.full/${var.gh_repo}",
    ]
  }
}

resource "google_service_account_iam_policy" "admin-account-iam" {
  service_account_id = google_service_account.runner_sa.name
  policy_data        = data.google_iam_policy.wli_user_ghshr.policy_data

  depends_on = [
    google_service_account.runner_sa
  ]
}

resource "google_project_iam_member" "project" {
  project = var.project_id
  role    = "roles/owner"
  member  = "serviceAccount:${google_service_account.runner_sa.email}"
}