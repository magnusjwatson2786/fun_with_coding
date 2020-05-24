public class obs {
  int lx=20, ly=375, x=(int(random(lx, ly))), y=(int(random(120, 475))), disap=0, dm=5;

  public void disp() {
    ellipseMode(RADIUS);  
    //col();  
    bar();
    if (disap>=dm) {
      gameover();
    }
    fill(0, 255, 0);
    ellipse(x, y, 5, 5);
  }//print(x+":"+y);}//gameover();}}
  public void ate() {
    x=(int(random(lx, ly)));
    y=(int(random(120, 475)));
    score++;
    barl=395;
  }//disap=0;}//p=q=r=0;}//}
  public void rec() {
    x=(int(random(lx, ly)));
    y=(int(random(120, 475)));
    barl=395;//p=q=r=0;////stopgame=false;}
  }
  //public void col(){if(r<=0){if(q<=0){rec();disap++;}else{q-=1;}}else{r-=1;}}
  public void bar() {
    if (barl<0) {
      rec();
      disap++;
    } else {
      barl-=bslp;
    }
    if (lvl==1) {
      dm=5;
    } else if (lvl==2) {
      dm=4;
    } else if (lvl==3) {
      bslp=1.5;
      dm=4;
    } else if (lvl==4) {
      bslp=1.5;
      dm=3;
    } else if (lvl==5) {
      bslp=2;
      dm=3;
    }
  }
}
