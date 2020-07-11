# Your Mission, convert this code to python

# const guess = (guess, target = 77) => {
#   if(guess > target) {
#     return 1;
#   }
#   if(guess < target) {
#     return -1;
#   }
#   return 0;
# }

# var guessNumber = function(n) {
#     let high = n;
#     let low = 1;
#     let mid = Math.floor(n / 2);
#     do {
#         if(guess(mid) === 1) {
#             high = mid;
#             mid = low + Math.floor((high - low) / 2);
#         }
#         if(guess(mid) === -1) {
#             low = mid;
#             mid = low + Math.floor((high - low) / 2);
#         }
#     } while (guess(mid) !== 0);
#     return mid;
# };

# guessNumber(100);