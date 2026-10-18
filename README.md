name: Deploy Pages

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: '18'

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./clientname: Build Android APK (TWA)

on:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup JDK
        uses: actions/setup-java@v3
        with:
          distribution: 'temurin'
          java-version: '11'

      - name: Install Node
        uses: actions/setup-node@v4
        with:
          node-version: '18'

      - name: Install Bubblewrap
        run: npm install -g @bubblewrap/cli

      - name: Init TWA project
        run: |
          mkdir -p twa_project
          cd twa_project
          npx @bubblewrap/cli init --manifest https://un-normal321.github.io/Mku/manifest.json --skip-keystore --directory .

      - name: Build APK
        run: |
          cd twa_project
          npx @bubblewrap/cli build --mode=dev

      - name: Upload APK artifact
        uses: actions/upload-artifact@v4
        with:
          name: mku-apk
          path: twa_project/platforms/android/app/build/outputs/apk/debug/*.apkmkdir -p .github/workflows
cat > .github/workflows/pages-deploy.yml <<'YAML'
name: Deploy Pages

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: '18'

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./client
YAML

cat > .github/workflows/android-build.yml <<'YAML'
name: Build Android APK (TWA)

on:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup JDK
        uses: actions/setup-java@v3
        with:
          distribution: 'temurin'
          java-version: '11'

      - name: Install Node
        uses: actions/setup-node@v4
        with:
          node-version: '18'

      - name: Install Bubblewrap
        run: npm install -g @bubblewrap/cli

      - name: Init TWA project
        run: |
          mkdir -p twa_project
          cd twa_project
          npx @bubblewrap/cli init --manifest https://un-normal321.github.io/Mku/manifest.json --skip-keystore --directory .

      - name: Build APK
        run: |
          cd twa_project
          npx @bubblewrap/cli build --mode=dev

      - name: Upload APK artifact
        uses: actions/upload-artifact@v4
        with:
          name: mku-apk
          path: twa_project/platforms/android/app/build/outputs/apk/debug/*.apkmkdir -p .github/workflows
cat > .github/workflows/pages-deploy.yml <<'YAML'
name: Deploy Pages

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: '18'

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./client
YAML

cat > .github/workflows/android-build.yml <<'YAML'
name: Build Android APK (TWA)

on:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup JDK
        uses: actions/setup-java@v3
        with:
          distribution: 'temurin'
          java-version: '11'

      - name: Install Node
        uses: actions/setup-node@v4
        with:
          node-version: '18'

      - name: Install Bubblewrap
        run: npm install -g @bubblewrap/cli

      - name: Init TWA project
        run: |
          mkdir -p twa_project
          cd twa_project
          npx @bubblewrap/cli init --manifest https://un-normal321.github.io/Mku/manifest.json --skip-keystore --directory .

      - name: Build APK
        run: |
          cd twa_project
          npx @bubblewrap/cli build --mode=dev

      - name: Upload APK artifact
        uses: actions/upload-artifact@v4
        with:
          name: mku-apk
          path: twa_project/platforms/android/app/build/outputs/apk/debug/*.apk
YAMLmkdir -p .github/workflows
cat > .github/workflows/pages-deploy.yml <<'YAML'
name: Deploy Pages

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: '18'

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./client
        

cat > .github/workflows/android-build.yml <<'YAML'
name: Build Android APK (TWA)

on:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup JDK
        uses: actions/setup-java@v3
        with:
          distribution: 'temurin'
          java-version: '11'

      - name: Install Node
        uses: actions/setup-node@v4
        with:
          node-version: '18'

      - name: Install Bubblewrap
        run: npm install -g @bubblewrap/cli

      - name: Init TWA project
        run: |
          mkdir -p twa_project
          cd twa_project
          npx @bubblewrap/cli init --manifest https://un-normal321.github.io/Mku/manifest.json --skip-keystore --directory .

      - name: Build APK
        run: |
          cd twa_project
          npx @bubblewrap/cli build --mode=dev

      - name: Upload APK artifact
        uses: actions/upload-artifact@v4
        with:
          name: mku-apk
          path: twa_project/platforms/android/app/build/outputs/apk/debug/*.apk
