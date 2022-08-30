# problem-solving-exercise1
Write a function that receives three inputs containing the text values A, B, and C. This function returns True only if the value of C is ordered parts of the values A and B. If the value C contains a part that is not in the values A and B, or present in an order that does not match the original order in A and B, the function returns False.
Example:
A = abc, B = dca, C = abdcca

When detailing the value C, we note that the value ab was subtracted from A, then the value dc was subtracted from B, then c from A again, and finally a from B. It does not matter which value the subtraction starts from, nor the amount of subtraction, the important thing is that it is the same The order in the original value, not more or less than the sum of the sums in the values A and B.
