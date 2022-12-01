import { Component, OnInit } from '@angular/core';
import { ProductService } from 'src/app/product.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  public productsArray:any = []
  

  constructor(private ProductService:ProductService) { }

  ngOnInit(): void {
    this.loadData();
  }

  public loadData(){
    this.ProductService.getProducts('https://stock-serviceutb.onrender.com/products/popular')
    .subscribe(response =>{
      this.productsArray = response;
      console.log(response);
    })
  }

}
