# Setup GFitrhub App

Option 1: GitHub App (Recommended)

  1. Create a GitHub App in your org/account settings (Settings > Developer settings > GitHub Apps)
  2. Give it Contents: write and Pull requests: write permissions
  3. Install it on your repo
  4. Store the App ID and private key as repo secrets:
    - APP_ID
    - APP_PRIVATE_KEY
  5. Update release.yml to generate a token from the App:

  steps:
    - name: Generate token
      id: generate-token
      uses: actions/create-github-app-token@v1
      with:
        app-id: ${{ secrets.APP_ID }}
        private-key: ${{ secrets.APP_PRIVATE_KEY }}

    - uses: actions/checkout@v4
      with:
        token: ${{ steps.generate-token.outputs.token }}
        fetch-depth: 0

    # ... rest of steps, replacing GITHUB_TOKEN:
    - name: Run semantic-release
      env:
        GITHUB_TOKEN: ${{ steps.generate-token.outputs.token }}
      run: npx semantic-release

