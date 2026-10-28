# Reflection: Pull Requests & Code Review

**1. Why is 'Squash and Merge' preferable over standard merge commits for small feature branches in team projects?**

A small feature usually picks up "wip" and "fix typo" commits along the way, and nobody needs those in main's history. Squashing turns the whole PR into one commit that describes the feature, so `git log` on main stays readable and the feature can be reverted with a single `git revert`.

**2. Describe the difference between 'Add single comment' and 'Start a review' on GitHub. Why is batching important?**

"Add single comment" posts the comment right away and sends a notification for each one. "Start a review" holds the comments as pending until you click "Finish your review", then sends them all together with one verdict (Comment, Approve, or Request changes). Batching keeps the author from getting a pile of separate emails, and they see the full feedback at once instead of starting fixes before the review is finished.

**3. How do Branch Protection Rules prevent accidental production breakage?**

They block direct pushes to main, so every change has to go through a pull request and get at least one approval before it can merge. A careless `git push origin main` gets rejected, and untested or unreviewed code can't reach the branch that gets deployed.

**4. When a remote conflict occurs in a PR, why is it better to merge origin/main into your feature branch locally rather than forcing a push?**

Merging origin/main brings your teammate's changes into your branch, so you resolve the conflict deliberately and can run the code before pushing. A force push rewrites history and can wipe out commits other people already built on, and it doesn't fix the conflict with main anyway. A normal push after the merge updates the PR and clears the conflict banner without destroying anyone's work.
