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
button_txt btnt2=new button_txt();
button_txt btnt3=new button_txt();
button_txt btnt4=new button_txt();
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
int s=20;

void setup(){
  size(1024,720); 
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
void mousePressed(){
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
  btnt2.mdata();
  btnt3.mdata();
  btnt4.mdata();
}
void mouseDragged(){
  noStroke();
  ellipse(mouseX,mouseY,s,s);
}
void draw() {
   
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
   btnt1.butt(125,125,25,50,'S');
   text("Brush Size:",250,137);
   btnt2.butt(315,125,25,25,'B');
   btnt3.butt(335,125,25,25,'C');
   btnt4.butt(355,125,25,25,'D');
   
  }
