public class button_txt{
  int mp=0,brc=0,cng=1;
  char mb;
  
  public void mdata(){
    this.mp=1;
    if(mouseButton==LEFT){
      this.mb='L';
    }
  }
  public void butt(int x,int y,int z,int a,char f){
    switch (f){
      case 'S':
        text("Save",x,y,x+z,y+a);
        break;
      case 'B':
        text("20",x,y,x+z,y+a);
        break;
      case 'C':
        text("40",x,y,x+z,y+a);
        break;
      case 'D':
        text("60",x,y,x+z,y+a);
        break;
    }
    if((mouseX >x) && (mouseX< (x+z))){
     if((mouseY >y) && (mouseY< (y+a))){
       cursor(HAND);
       if(this.mp==1 && this.mb=='L'){
         print("That was a left click!");
         switch (f){
            case 'S':
              saveFrame("img-#####");
              break;
            case 'B':
              s=20;
              break;
            case 'C':
              s=40;
              break;
            case 'D':
              s=60;
              break;
          }
           
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
