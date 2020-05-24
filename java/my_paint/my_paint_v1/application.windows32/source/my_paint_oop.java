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

public class my_paint_oop extends PApplet {

button btn1=new button();
button btn2=new button();
button btn3=new button();
button btn4=new button();
button btn5=new button();
button btn6=new button();
button btn7=new button();
button btn8=new button();
button btn9=new button();
PImage i1;
PImage i2;
PImage i3;
PImage i4;
PImage i5;
PImage i6;
PImage i7;
PImage i8;
PImage i9;
PImage j1;

public void setup(){
   
  frameRate(200);
  background(255);
  i1 = loadImage("0,0,0.png");
  i2 = loadImage("255,0,0.png");
  i3 = loadImage("255,255,0.png");
  i4 = loadImage("0,162,232.png");
  i5 = loadImage("0,255,0.png");
  i6 = loadImage("136,0,21.png");
  i7 = loadImage("255,0,128.png");
  i8 = loadImage("255,255,255.png");
  i9 = loadImage("0,0,255.png");
  j1 = loadImage("bck.png");
  image(j1, 0, 0);
  image(i1, 0, 0);
  image(i2, 100, 0);
  image(i3, 200, 0);
  image(i4, 300, 0);
  image(i5, 400, 0);
  image(i6, 500, 0);
  image(i7, 600, 0);
  image(i8, 700, 0);
  image(i9, 800, 0);
}
public void mousePressed(){
  btn1.mdata();
  btn2.mdata();
  btn3.mdata();
  btn4.mdata();
  btn5.mdata();
  btn6.mdata();
  btn7.mdata();
  btn8.mdata();
  btn9.mdata();
}
public void mouseDragged(){
  noStroke();
  ellipse(mouseX,mouseY,20,20);
}
public void draw() {
   
   btn1.butt(0,0,100,100,0,0,0);
   btn2.butt(100,0,100,100,255,0,0);
   btn3.butt(200,0,100,100,255,255,0);
   btn4.butt(300,0,100,100,0,162,232);
   btn5.butt(400,0,100,100,0,255,0);
   btn6.butt(500,0,100,100,136,0,21);
   btn7.butt(600,0,100,100,255,0,128);
   btn8.butt(700,0,100,100,255,255,255);
   btn9.butt(800,0,100,100,0,0,255);
   
   
   noStroke();
   image(j1, 0, 0);
   image(i1, 0, 0);
   image(i2, 100, 0);
   image(i3, 200, 0);
   image(i4, 300, 0);
   image(i5, 400, 0);
   image(i6, 500, 0);
   image(i7, 600, 0);
   image(i8, 700, 0);
   image(i9, 800, 0);
  }
public class button{
  private int mp=0;
  private char mb;
  private char name;
  
  public void mdata(){
    this.mp=1;
    if(mouseButton==LEFT){
      this.mb='L';
    }
    
  }
  public void butt(int x,int y,int z,int a,int p,int q,int r){
    if((mouseX >x) && (mouseX< (x+z))){
     if((mouseY >y) && (mouseY< (y+a))){
       cursor(CROSS);
       if(this.mp==1 && this.mb=='L'){
         fill(p,q,r);
         print("clicked");
       }
     }
     else{
     cursor(ARROW);
     }
   }

  this.mp=0;
  this.mb='a';
  
 }
}
  public void settings() {  size(1024,720); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "my_paint_oop" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
