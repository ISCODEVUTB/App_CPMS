import { Component, OnInit } from '@angular/core';
import { ProductService } from 'src/app/product.service';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent implements OnInit {

  public productsArray:any = []

  constructor(private ProductService:ProductService) { }

  ngOnInit(): void {
    this.loadData();
  }

  public loadData(){
    this.ProductService.getProducts('https://stock-serviceutb.onrender.com/products/')
    .subscribe(response =>{
      this.productsArray = response;
      console.log(response);
    })
  }

}
