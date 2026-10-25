# Step-by-step: VS Code to GitHub

This guide assumes Windows and VS Code. The commands are run in the VS Code terminal from the project root.

## Part 1 — Download and extract

1. Download the project ZIP.
2. Open your Downloads folder.
3. Right-click the ZIP and choose **Extract All**.
4. Open VS Code.
5. Select **File → Open Folder**.
6. Choose the extracted `EWB_Library_Book_Management_API` folder.
7. Confirm that you can see `app`, `tests`, `requirements.txt`, and `README.md` in the Explorer panel.

## Part 2 — Check Python and Git

1. In VS Code, select **Terminal → New Terminal**.
2. Run:

```powershell
py --version
git --version
```

If either command is not recognized, install Python from the official Python website and Git from the official Git website, then restart VS Code. During Python installation on Windows, enable the option to add Python to PATH if it is offered.

## Part 3 — Create the virtual environment and install packages

Run each command separately in the terminal:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If PowerShell refuses to activate the environment, switch the VS Code terminal profile to **Command Prompt**, open a new terminal, and run:

```bat
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
```

A terminal prompt that starts with `(.venv)` indicates that the virtual environment is active.

## Part 4 — Run and test the API

Start the server:

```powershell
python -m uvicorn app.main:app --reload
```

Keep this terminal open while the server runs. In your browser, open `http://127.0.0.1:8000/docs`.

Try the following in Swagger UI:

1. Open `POST /books/`, click **Try it out**, paste the sample JSON from `README.md`, then click **Execute**. Expect `201`.
2. Open `GET /books/` and execute it. Expect a list containing the book.
3. Open `GET /books/{book_id}` and enter the `book_id` returned by step 1.
4. Open `PUT /books/{book_id}` and send the full book JSON with a changed title.
5. Open `DELETE /books/{book_id}` and enter the ID.
6. Try `GET /books/99999`. Expect `404 Book not found` if that ID does not exist.

Stop the server with `Ctrl+C` in its terminal. Run the tests:

```powershell
python -m pytest -v
```

Do not continue to GitHub until the app starts successfully and tests pass.

## Part 5 — Create the GitHub repository

1. Sign in to GitHub or create an account on GitHub's official website.
2. Click the **+** menu near the top-right and choose **New repository**.
3. Repository name: `ewb-library-book-management-api`
4. Description: `Library Book Management REST API built with FastAPI and SQLite`
5. Choose **Public** if you want your professor to view it without signing in, or **Private** if you want to limit access.
6. For this workflow, leave **Add a README**, **.gitignore**, and **license** unchecked because your local project already has files.
7. Click **Create repository**.
8. Keep the new repository page open. GitHub will show its repository address and setup instructions.

## Part 6 — Set up Git locally

Make sure the VS Code terminal is in the project root. Check with:

```powershell
pwd
```

You should see a path ending in `EWB_Library_Book_Management_API`.

Set your Git identity (use the name and email you want associated with your commits):

```powershell
git config --global user.name "Your Name"
git config --global user.email "your-github-email@example.com"
```

Replace the example values with your own. Your commit email can be configured in GitHub settings if you prefer to keep your personal email private.

Initialize Git and check what will be tracked:

```powershell
git init
git status
```

Add files and make your first commit:

```powershell
git add .
git status
git commit -m "Initial commit: library book management API"
```

**Check before `git add .`:** `git status` should not show `.venv/`, `library.db`, passwords, API keys, or personal files. The included `.gitignore` excludes common local files. Never upload secrets.

## Part 7 — Connect the local project to GitHub

On the GitHub repository page, copy the repository URL. It looks like `https://github.com/YOUR-USERNAME/ewb-library-book-management-api.git`. Use your actual URL in the command below:

```powershell
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/ewb-library-book-management-api.git
git push -u origin main
```

If GitHub asks you to authenticate, follow the browser sign-in prompt or Git Credential Manager. Do not paste your password or access token into a public file or chat.

Refresh the GitHub repository page. You should see the folders, Python files, `README.md`, and tests.

## Part 8 — Make and publish a change

1. Open `README.md` in VS Code.
2. Add a small improvement, such as a note explaining that `available=true` filters available books.
3. Save the file.
4. In the terminal, run:

```powershell
git status
git add README.md
git commit -m "Improve API usage documentation"
git push
```

5. Refresh GitHub and confirm the change appears.

This is the normal cycle: **edit → save → `git add` → `git commit` → `git push`**.

## Common problems

- **`git` is not recognized:** install Git, restart VS Code, and run `git --version`.
- **`py` is not recognized:** install Python and reopen the terminal; on some systems use `python` instead of `py`.
- **PowerShell script execution is blocked:** switch the VS Code terminal to Command Prompt and use `.venv\\Scripts\\activate.bat`.
- **`remote origin already exists`:** run `git remote -v` to inspect it. If it is the wrong URL, use `git remote set-url origin YOUR-REPOSITORY-URL`.
- **Push is rejected because GitHub already has a README:** this usually happens if you initialized files on GitHub as well. The easiest beginner-safe route is to create an empty repository as described above. If this has already happened, stop and inspect the error before trying more commands.
- **Authentication failed:** follow GitHub's browser-based authentication or Git Credential Manager prompt. GitHub does not accept your account password as Git HTTPS authentication.
- **A database file appears in Git status:** stop before committing; check `.gitignore` and ensure the database file is not staged.

## Part 9 — What to tell your professor

> I built a Library Book Management REST API using FastAPI, SQLAlchemy, and SQLite. It supports create, read, update, and delete operations, plus filters for title, author, category, and availability. Pydantic validates incoming data, duplicate ISBNs are rejected, and missing records return a 404 response. I added automated tests and published the source code to GitHub. The README explains how to install, run, and test the application.

## Final checklist

- [ ] App starts with Uvicorn.
- [ ] `/docs` opens.
- [ ] Create, list, read, update, and delete work.
- [ ] `python -m pytest -v` passes.
- [ ] GitHub repository exists.
- [ ] README and source files appear on GitHub.
- [ ] No `.venv`, database, secrets, or private data are uploaded.
- [ ] A second commit was pushed successfully.
