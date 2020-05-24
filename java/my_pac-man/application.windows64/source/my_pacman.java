import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class my_pacman extends PApplet {

//My Pac-Man
//this is a sample game using Processing Java Graphics
//Created by Johannes Schimidth on 7/2/2019
PImage pac_c_r;
PImage mpl;
PImage pac_o_r;
PImage pac_c_l;
PImage pac_o_l;
PImage pac_c_u;
PImage pac_o_u;
PImage pac_c_d;
PImage pac_o_d;
int time=0, imgs=0, imgo=0, score=0, lvl=1, barl=395;
obj ob1 = new obj();
obs os1 =new obs();
float d, bslp=1;
boolean stopgame=false;
public void setup() {
  
  restart();
  pac_c_r=loadImage("pac_c_r.png");
  pac_o_r=loadImage("pac_o_r.png");
  pac_c_l=loadImage("pac_c_l.png");
  pac_o_l=loadImage("pac_o_l.png");
  pac_c_u=loadImage("pac_c_u.png");
  pac_o_u=loadImage("pac_o_u.png");
  pac_c_d=loadImage("pac_c_d.png");
  pac_o_d=loadImage("pac_o_d.png");
  mpl=loadImage("mypaclogo.png");
  
}

public void keyPressed() {
  if (keyCode==ENTER) {
    restart();
  }
}

public void draw() {
  if (stopgame) {
  } else {
    d=dist(ob1.x, ob1.y, os1.x, os1.y);
    if (d<17.5f) {
      os1.ate();
    }
    if (score>30) {
      lvl=2;
    }
    if (score>50) {
      lvl=3;
    }
    if (score>70) {
      lvl=4;
    }
    if (score>90) {
      lvl=5;
    }
    background(0);
    fill(230, 40, 40);
    rect(0, 100, 400, 400);
    fill(0);
    rect(10, 110, 380, 380);
    os1.disp();
    ob1.move();
    ob1.kdata();
    time++;
    if (time%10==0) {
      if (imgs==0) {
        imgs=1;
      } else {
        imgs=0;
      }
    }
    //println("--"+score);
    fill(0, 140, 255);
    rect(5, 505, barl, 5);
    //barl-=1;
    fill(0, 255, 140);
    text("Help the PacMan eating his food.", 0, 530);
    text("Avoid the red boundary! and Eat food before the above bar's empty.", 0, 550);
    text("Score: "+score, 15, 575);
    text("Level: "+lvl, 75, 575);
    text("Misses Allowed: "+os1.dm, 135, 575);
    text("Times Missed: "+os1.disap, 275, 575);
  }
image(mpl,0,0);
}


public void gameover() {
  stopgame=true;
  fill(255);
  text("GAME OVER!", 150, 205);
  text("Score:  "+str(score), 165, 235);
  text("Press ENTER to RESTART", 120, 255);
}

public void restart() {
  stopgame=false;
  time=0;
  imgs=0;
  imgo=0;
  score=0;
  os1.rec();
  ob1.x=200;
  ob1.y=300;
  os1.disap=0;
  lvl=1;
}
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
public class obs {
  int lx=20, ly=375, x=(PApplet.parseInt(random(lx, ly))), y=(PApplet.parseInt(random(120, 475))), disap=0, dm=5;

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
    x=(PApplet.parseInt(random(lx, ly)));
    y=(PApplet.parseInt(random(120, 475)));
    score++;
    barl=395;
  }//disap=0;}//p=q=r=0;}//}
  public void rec() {
    x=(PApplet.parseInt(random(lx, ly)));
    y=(PApplet.parseInt(random(120, 475)));
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
      bslp=1.5f;
      dm=4;
    } else if (lvl==4) {
      bslp=1.5f;
      dm=3;
    } else if (lvl==5) {
      bslp=2;
      dm=3;
    }
  }
}
  public void settings() {  size(400, 600); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "my_pacman" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
