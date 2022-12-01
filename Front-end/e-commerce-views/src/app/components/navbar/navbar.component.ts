import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  isLoggedIn = false

  txtValue = null
  
  isEmpty = true

  name:string = "";

  onTextChange(value:any)
  {
    this.txtValue = value;
    if(this.txtValue == '')
    {
      this.isEmpty = false
    }
    
  }

  public onLogOut(){
    this.isLoggedIn = !this.isLoggedIn
  }

  ngOnInit(): void {
  }

  onSubmit(event:any){
    this.name = event.target.name.value;

  }

}
