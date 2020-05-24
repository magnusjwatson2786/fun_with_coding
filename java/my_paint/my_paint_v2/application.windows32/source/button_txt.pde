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
