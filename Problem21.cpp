#include <iostream>
#include <cmath>

// SOLVED

//Let d(n) be defined as the sum of proper divisors of n(numbers less than n which divide evenly into n).
//If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

//For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
//therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

//Evaluate the sum of all the amicable numbers under 10000.


using namespace std;

int main() {
	int sumOne = 0;
	int sumTwo = 0;
	int target = 0;
	int sumA = 0;
	int limit = 10001;
	int temp = 0;

	for (int j = 219; j < limit; j++) {
		target = j;
		sumOne = 0;
		sumTwo = 0;

		if (j == temp) {
			continue;
		}

		if (j % 2 != 0) { // no amicable pair under 10000 is odd
			continue;
		}

		//cout << "Target is: " << target << endl;

		for (int i = 1; i <= (target / 2); i++) {
			if ((target % i) == 0) {
				//cout << i << endl;
				sumOne += i;
			}
			else {

			}
		}

		//cout << "SUMONE IS: " << sumOne << endl;

		//cout << "Target is: " << sumOne << endl;

		for (int i = 1; i <= (sumOne / 2); i++) {
			if ((sumOne % i) == 0) {
				//cout << i << endl;
				sumTwo += i;
			}
			else {

			}
		}

		//cout << "SUMTWO IS: " << sumTwo << endl;

		if (sumTwo == target && sumOne != target) {
			cout << target << " and " << sumOne << " are amicable" << endl;
			temp = sumOne;
			sumA += target + sumOne;
			cout << "Their sum is: " << sumA << endl;
		}
		else {
			//cout << "Not amicable" << endl;
		}
	}



}