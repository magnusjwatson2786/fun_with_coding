public class obj {
  int x=200, y=300, sp=3;
  public void kdata() {

    if (key == CODED) {
      if (keyCode == RIGHT) {
        x+=sp;
        imgo=0;
      } else if (keyCode == LEFT) {
        imgo=2;
        x-=sp;
      } else if (keyCode == UP) {
        y-=sp;
        imgo=1;
      } else if (keyCode == DOWN) {
        y+=sp;
        imgo=3;
      }
    }
  }
  public void move() {
    chk();
    bound();
    if (imgs==0&&imgo==0) {
      image(pac_c_r, x, y);
    } else if (imgs==1&&imgo==0) {
      image(pac_o_r, x, y);
    } else if (imgs==1&&imgo==1) {
      image(pac_o_u, x, y);
    } else if (imgs==0&&imgo==1) {
      image(pac_c_u, x, y);
    } else if (imgs==1&&imgo==2) {
      image(pac_o_l, x, y);
    } else if (imgs==0&&imgo==2) {
      image(pac_c_l, x, y);
    } else if (imgs==1&&imgo==3) {
      image(pac_o_d, x, y);
    } else if (imgs==0&&imgo==3) {
      image(pac_c_d, x, y);
    }
  }
  public void bound () {
    if (x<=5) {
      x=5;
    } 
    if (x>=375) {
      x=375;
    } 
    if (y<=105) {
      y=105;
    } 
    if (y>=475) {
      y=475;
    }
  }

  public void chk() {
    if (x<=10|| (x>=370) || (y<=110) || (y>=470)) {
      gameover();
    }
  }
}
