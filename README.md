# html-cleaning
Basic Python script to extract plain text and clean up white space from a repo of HTML files.

To use, edit line 6 to reflect the path to and name of the repo containing the html files; and line 15 to reflect the actual repo name and desired new reponame. If necessary, edit line 19 to reflect desired changes or comment out to reflect desired lack of change, in the final file extension.

Improvements I'll make to this file if I ever think it'll be worthwhile:
  1.) improve the progress bar. Basic tqdm on the outermost loop is a decent-but-not-great solution. It's main benefit was that I could get it working in ~10 seconds.
  2.) taking in directory_name and new-reponame as arguments instead of being hardcoded. Not worth it for this project, as it was a one-off script for a bespoke dataset, but would have been nice to have if it had been worth the time.
  
I would also potentially like to make it a more functional script which allows users to select exactly which changes they'd like to make to the files, but that would be significant overkill for the intent of this project.
