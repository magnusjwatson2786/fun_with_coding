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
void setup() {
  size(400, 600);
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

void keyPressed() {
  if (keyCode==ENTER) {
    restart();
  }
}

void draw() {
  if (stopgame) {
  } else {
    d=dist(ob1.x, ob1.y, os1.x, os1.y);
    if (d<17.5) {
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


void gameover() {
  stopgame=true;
  fill(255);
  text("GAME OVER!", 150, 205);
  text("Score:  "+str(score), 165, 235);
  text("Press ENTER to RESTART", 120, 255);
}

void restart() {
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
