import g4p_controls.*;
int s=20;
int p,q,r;
int sh=0;

public void setup(){
  size(1024, 720, JAVA2D);
  createGUI();
  customGUI();
  background(255);
}

void mousePressed(){
  
}
void mouseDragged(){
  fill(p,q,r);
  noStroke();
  if(sh==1){
    rect(mouseX,mouseY,s,s);}
  else
    {ellipse(mouseX,mouseY,s,s);}
}

public void draw(){
  
  
}

public void customGUI(){

}
