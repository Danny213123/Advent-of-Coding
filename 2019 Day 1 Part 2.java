import java.util.Scanner;

class Main {
  public static void main(String[] args) {

    Scanner in = new Scanner(System.in); int a = 0;

    for (int x = 0; x < 100; x++){
      a += (Recursion(in.nextInt()));
    }

    System.out.print (a);
  }

  static int Recursion(int n){
    if (n <= 0){
      return n;
    } else {
      return (((n / 3) - 2) + Recursion((n / 3) - 2));
    }
  }
}
