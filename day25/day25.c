#include <stdio.h>

int MOD=20201227;
int SUBJ=7;

int A=6930903;
int B=19716708;

long powm(long base, unsigned long exp, long modulus) {
  base %= modulus;
  long result = 1;
  while (exp > 0) {
    if (exp & 1) result = (result * base) % modulus;
    base = (base * base) % modulus;
    exp >>= 1;
  }
  return result;
}

int main() {
  int a=1,b=1;
  int secret=0;
  while(1) {
    if (secret%1000000 == 0) printf("...%d\n",secret);
    if (a==A) {
      printf("a %d,%d: %d\n",a,A,secret);
      printf("1--->%d\n",powm(B,secret,MOD));
      break;
    }
    if (b==B) {
      printf("b %d,%d: %d\n",b,B,secret);
      printf("1--->%d\n",powm(A,secret,MOD));
      break;
    }
    a = (a*SUBJ)%MOD;
    b = (b*SUBJ)%MOD;
    ++secret;
  }
}
