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
