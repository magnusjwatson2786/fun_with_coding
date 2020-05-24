// Need G4P library
import g4p_controls.*;
// You can remove the PeasyCam import if you are not using
// the GViewPeasyCam control or the PeasyCam library.
int s=20;
int p,q,r;
int sh=1;

public void setup(){
  size(1024,720,JAVA2D);
  createGUI();
  customGUI();
  background(255);
  // Place your setup code here
  
}

void mousePressed(){
  
}
void mouseDragged(){
  noStroke();
  if(sh==0){
    rect(mouseX,mouseY,s,s);}
  else
    {ellipse(mouseX,mouseY,s,s);}
}
void draw() {
  fill(210,210,210);
  rect(0,0,1024,100);
  fill(p,q,r);
  rect(40,20,60,60);
}
// Use this method to add additional statements
// to customise the GUI controls
public void customGUI(){

}
