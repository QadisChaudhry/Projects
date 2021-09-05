#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
using namespace std;

int main () {
  int number, guess, tries;
  string username;
  string question;
  srand (time(NULL));
  number = rand() % 10 + 1;
  tries = 1;

  cout << "Hello, what is your name? ";
  cin >> username;
  cout << "Hello " << username << "!" << endl;

  cout << "Would you like to play a game...? [y/n] ";
  cin >> question;
  if (question == "y") {
      cout << "Yay! I'm thinking of a number between 1 & 10... " << endl;
      cout << "Take a Guess... ";
      cin >> guess;
  }
  else {
      cout << "Oh.. okay..." << endl;
      return 0;
  }

  if (guess < number) {
      cout << "Guess a little higher... ";
      tries += 1;
      cin >> guess;
  }
  if (guess > number) {
      cout << "Guess a little lower... ";
      tries += 1;
      cin >> guess;
  }

  while (guess != number) {
      cout << "Try again... ";
      tries += 1;
      cin >> guess;
  }

  if (guess == number) {
      cout << "You did it! The number was " << number << " and it only took you " << tries;
      if (tries == 1) {
          cout << " try!" << endl;
      }
      else {
          cout << " tries!" << endl;
      }
  }

return 0;
}
