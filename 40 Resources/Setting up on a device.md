---
type: reference
---
# Setting up on a device

How to get this brain onto Bradley's Windows laptop and iPhone. The vault lives in a private GitHub repository, `github.com/ehijeleb/bradley-second-brain`, and Bradley has access as a collaborator.

## 1. Get access (once)
1. Bradley makes a free account at https://github.com if he doesn't have one, and sends his username to the repository owner.
2. The owner goes to the repository, **Settings, Collaborators, Add people**, and adds that username.
3. Bradley accepts the invite (email from GitHub, or https://github.com/notifications).

## 2. Windows laptop
1. **Install Git** from https://git-scm.com with the default options (it includes the sign-in helper). Install **Python 3** from https://python.org with "Add python.exe to PATH" ticked (only needed for the Excel export).
2. **Clone the vault.** Open PowerShell in your user folder and run (swap `BRADLEYS-USERNAME` for your GitHub username):
   ```
   git clone https://BRADLEYS-USERNAME@github.com/ehijeleb/bradley-second-brain.git bradleys-brain
   cd bradleys-brain
   git config user.name "Bradley Duke"
   git config user.email "BRADLEYS-USERNAME@users.noreply.github.com"
   ```
   A browser window asks you to sign in to GitHub the first time. Use your own account.
3. **Open it in Obsidian:** "Open folder as vault", pick `bradleys-brain`, and trust the author.
4. **Plugins:** Settings, Community plugins, turn off Restricted mode, then Browse and install and enable:
   - **Git** (by Vinzent): set "Auto commit-and-sync interval" to 10 minutes and turn on "Pull on startup".
   - **Dataview**: turn on **Enable JavaScript queries** (the Reselling and Finance tables need it).
5. **Core settings:**
   - Core plugins: **Bases**, **Templates** and **Daily notes** on (update Obsidian if Bases is missing).
   - Templates: folder `Templates`.
   - Daily notes: folder `01 Daily`, template `Templates/Daily`, date format `YYYY-MM-DD`.
   - Files and links: new attachments go in `Attachments`.
6. **Excel export (once):** `python -m pip install openpyxl`.
7. **Claude Code:** start it in the `bradleys-brain` folder. It reads `CLAUDE.md`, knows whose brain this is, and walks through [[Start here]].

## 3. iPhone
- **Claude:** in the Claude app's Code section, connect GitHub (your account) and pick `ehijeleb/bradley-second-brain`. Claude pulls, edits, then commits and pushes, and the laptop picks the changes up on its next sync.
- **Obsidian on the phone (optional):** two choices.
  - **Obsidian Git on mobile:** free, but slower and fiddlier. It needs a GitHub personal access token (fine-grained, Contents read and write, this repository only), which you paste into the plugin yourself.
  - **Obsidian Sync:** paid, the smoothest option. Keep Git on the laptop as the backup.
  - Or skip it, and use the phone only through Claude.

## Keeping it in sync
- The laptop syncs itself every 10 minutes while Obsidian is open, and pulls when Obsidian starts.
- If Claude edits in the cloud while Obsidian has unsynced changes, Git may report a conflict. Open the Git panel, pull, then sync. Ask Claude to help if it gets stuck.
