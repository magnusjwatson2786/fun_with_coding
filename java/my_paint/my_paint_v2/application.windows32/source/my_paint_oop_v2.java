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

public class my_paint_oop_v2 extends PApplet {

button_img btni1=new button_img();
button_img btni2=new button_img();
button_img btni3=new button_img();
button_img btni4=new button_img();
button_img btni5=new button_img();
button_img btni6=new button_img();
button_img btni7=new button_img();
button_img btni8=new button_img();
button_img btni9=new button_img();
button_txt btnt1=new button_txt();
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
  btni1.mdata();
  btni2.mdata();
  btni3.mdata();
  btni4.mdata();
  btni5.mdata();
  btni6.mdata();
  btni7.mdata();
  btni8.mdata();
  btni9.mdata();
  btnt1.mdata();
}
public void mouseDragged(){
  noStroke();
  ellipse(mouseX,mouseY,20,20);
}
public void draw() {
   
   btni1.butt(0,0,100,100,0,0,0);
   btni2.butt(100,0,100,100,255,0,0);
   btni3.butt(200,0,100,100,255,255,0);
   btni4.butt(300,0,100,100,0,162,232);
   btni5.butt(400,0,100,100,0,255,0);
   btni6.butt(500,0,100,100,136,0,21);
   btni7.butt(600,0,100,100,255,0,128);
   btni8.butt(700,0,100,100,255,255,255);
   btni9.butt(800,0,100,100,0,0,255);
   
   
   
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
   btnt1.butt(125,125,25,50);
  }
public class button_img{
  private int mp=0;
  private char mb;
  
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
public class button_txt{
  private int mp=0;
  private char mb;
  
  public void mdata(){
    this.mp=1;
    if(mouseButton==LEFT){
      this.mb='L';
    }
  }
  public void butt(int x,int y,int z,int a){
    text("Save",x,y,x+z,y+a);
    if((mouseX >x) && (mouseX< (x+z))){
     if((mouseY >y) && (mouseY< (y+a))){
       cursor(HAND);
       if(this.mp==1 && this.mb=='L'){
         print("That was a left click!");
         saveFrame("img-#####");
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
    String[] appletArgs = new String[] { "my_paint_oop_v2" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
