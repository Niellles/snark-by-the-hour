# Snark by the hour
Inspired by [Davy M](https://meta.stackoverflow.com/users/7795130/davy-m).'s [post](https://meta.stackoverflow.com/questions/369938/now-that-we-can-detect-snark-what-are-we-planning-to-do-with-it) on Stack Overflow Meta as a reaction on SO's June Update. I've decided to make the _Snark by the hour_ feed happen.
It seems like a fun thing to make and I really couldn't agree more with Davy's words:
> My idea is a Snark by the Hour live feed so I can enjoy the sarcasm and snark of my favorite Stack Overflow users in real time, but that's just me.

If you happen to have a snarkiness-classifier (with a training set) laying around, feel free to let me now in an issue, or better yet; throw me a pull request. (_Yes, kind people of SO, I am hinting at you guys here._)

## To-do:
- [ ] Gather some training data
  - [x] Code data collector
    - [ ] Hopefully improve this if this [API issue](https://stackoverflow.com/questions/51269945/order-stackexchange-api-reponse-by-date-and-specify-minimum-votes) ever gets fixed. Or find a work around ? Which is not too hard for comments that have been added since the collectors last run.
  - [x] Extract possible features
     - [ ] Determine sarcasm. (Waiting for my [pull request](https://github.com/AniSkywalker/SarcasmDetection/pull/4) to AniSkywalker/SarcasmDetection to be merged.)
  - [ ] Clean-up code and make seperate modules for collection and feature extraction
  - [ ] Grab data from API
  - [ ] Manually rate a [metric shit ton](http://supremecourtjester.blogspot.com/2015/05/units-of-modern-measurement-how-many.html) of comments.
- [ ] Come up with a snarkiness classifier
  - [ ] Visualize data.
  - [ ] Select relevant features
  - [ ] Determine appropriate classifier
- [ ] Make some web interface to show this potentially hilarious data
- [ ] Write a classifier for questions that are likely to yield snarky comments
