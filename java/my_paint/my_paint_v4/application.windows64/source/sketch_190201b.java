import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import g4p_controls.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class sketch_190201b extends PApplet {

// Need G4P library

// You can remove the PeasyCam import if you are not using
// the GViewPeasyCam control or the PeasyCam library.
int s=20;
int p,q,r;
int sh=1;

public void setup(){
  
  createGUI();
  customGUI();
  background(255);
  // Place your setup code here
  
}

public void mousePressed(){
  
}
public void mouseDragged(){
  noStroke();
  if(sh==0){
    rect(mouseX,mouseY,s,s);}
  else
    {ellipse(mouseX,mouseY,s,s);}
}
public void draw() {
  fill(210,210,210);
  rect(0,0,1024,100);
  fill(p,q,r);
  rect(40,20,60,60);
}
// Use this method to add additional statements
// to customise the GUI controls
public void customGUI(){

}
/* =========================================================
 * ====                   WARNING                        ===
 * =========================================================
 * The code in this tab has been generated from the GUI form
 * designer and care should be taken when editing this file.
 * Only add/edit code inside the event handlers i.e. only
 * use lines between the matching comment tags. e.g.

 void myBtnEvents(GButton button) { //_CODE_:button1:12356:
     // It is safe to enter your event code here  
 } //_CODE_:button1:12356:
 
 * Do not rename this tab!
 * =========================================================
 */


public void button2_click1(GButton source, GEvent event) { //_CODE_:button2:394409:
  saveFrame("img-#####");
} //_CODE_:button2:394409:

public void button3_click1(GButton source, GEvent event) { //_CODE_:button2:394409:
  p=255;
  q=255;
  r=255;
} //_CODE_:button2:394409:

public void button4_click1(GButton source, GEvent event) { //_CODE_:button2:394409:
  sh=1;}

public void button5_click1(GButton source, GEvent event) { //_CODE_:button2:394409:
  sh=0;}

public void slider1_change1(GSlider source, GEvent event) { //_CODE_:slider5:704179:
  s=source.getValueI();
} //_CODE_:slider5:704179:

public void slider2_change1(GSlider source, GEvent event) { //_CODE_:slider5:809907:
  p=source.getValueI();
} //_CODE_:slider5:809907:

public void slider3_change1(GSlider source, GEvent event) { //_CODE_:slider6:442384:
  q=source.getValueI();
} //_CODE_:slider6:442384:

public void slider4_change1(GSlider source, GEvent event) { //_CODE_:slider5:980845:
  r=source.getValueI();
} //_CODE_:slider5:980845:



// Create all the GUI controls. 
// autogenerated do not edit
public void createGUI(){
  G4P.messagesEnabled(false);
  G4P.setGlobalColorScheme(GCScheme.BLUE_SCHEME);
  G4P.setMouseOverEnabled(false);
  surface.setTitle("MyPaint v4");
  button2 = new GButton(this, 904, 72, 48, 24);
  button2.setText("Save");
  button2.setTextBold();
  button2.addEventHandler(this, "button2_click1");
  button3 = new GButton(this, 274,30,72,24);
  button3.setText("Eraser");
  button3.setTextBold();
  button3.addEventHandler(this, "button3_click1");
  button4 = new GButton(this, 465,20,72,24);
  button4.setText("Elliptical");
  button4.setTextBold();
  button4.addEventHandler(this, "button4_click1");
  button5 = new GButton(this, 465,50,80,24);
  button5.setText("Rectangular");
  button5.setTextBold();
  button5.addEventHandler(this, "button5_click1");
  label2= new GLabel(this, 555, 32, 80, 20);
  label2.setTextAlign(GAlign.CENTER, GAlign.MIDDLE);
  label2.setText("Brush size:");
  label2.setOpaque(false);
  label6= new GLabel(this, 385, 32, 80, 20);
  label6.setTextAlign(GAlign.CENTER, GAlign.MIDDLE);
  label6.setText("Brush shape:");
  label6.setOpaque(false);
  slider1 = new GSlider(this, 625, 24, 100, 40, 10.0f);
  slider1.setShowValue(true);
  slider1.setLimits(20.0f, 5.0f, 100.0f);
  slider1.setNbrTicks(20);
  slider1.setNumberFormat(G4P.DECIMAL, 2);
  slider1.setOpaque(false);
  slider1.addEventHandler(this, "slider1_change1");
  label3 = new GLabel(this, 88, 16, 80, 20);
  label3.setTextAlign(GAlign.CENTER, GAlign.MIDDLE);
  label3.setText("R:");
  label3.setTextBold();
  label3.setOpaque(false);
  label4 = new GLabel(this, 88, 40, 80, 20);
  label4.setTextAlign(GAlign.CENTER, GAlign.MIDDLE);
  label4.setText("G:");
  label4.setTextBold();
  label4.setOpaque(false);
  label5 = new GLabel(this, 88, 64, 80, 20);
  label5.setTextAlign(GAlign.CENTER, GAlign.MIDDLE);
  label5.setText("B:");
  label5.setTextBold();
  label5.setOpaque(false);
  slider2 = new GSlider(this, 144, 8, 100, 40, 10.0f);
  slider2.setShowValue(true);
  slider2.setLimits(0.0f, 0.0f, 255.0f);
  slider2.setNbrTicks(51);
  slider2.setNumberFormat(G4P.DECIMAL, 1);
  slider2.setOpaque(false);
  slider2.addEventHandler(this, "slider2_change1");
  slider3= new GSlider(this, 144, 32, 100, 40, 10.0f);
  slider3.setShowValue(true);
  slider3.setLimits(0.0f, 0.0f, 255.0f);
  slider3.setNbrTicks(51);
  slider3.setNumberFormat(G4P.DECIMAL, 1);
  slider3.setOpaque(false);
  slider3.addEventHandler(this, "slider3_change1");
  slider4 = new GSlider(this, 144, 56, 100, 40, 10.0f);
  slider4.setShowValue(true);
  slider4.setLimits(0.0f, 0.0f, 255.0f);
  slider4.setNbrTicks(51);
  slider4.setNumberFormat(G4P.DECIMAL, 1);
  slider4.setOpaque(false);
  slider4.addEventHandler(this, "slider4_change1");
}

// Variable declarations 
// autogenerated do not edit
GButton button2;
GButton button3;
GButton button4;
GButton button5;
GLabel label2; 
GSlider slider1; 
GLabel label3; 
GLabel label4; 
GLabel label5; 
GLabel label6; 
GSlider slider2; 
GSlider slider3; 
GSlider slider4; 
  public void settings() {  size(1024,720,JAVA2D); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "sketch_190201b" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
