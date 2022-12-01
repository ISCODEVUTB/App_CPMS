import { Component, OnInit } from '@angular/core';
import { ProductService } from 'src/app/product.service';

@Component({
  selector: 'app-hogar',
  templateUrl: './hogar.component.html',
  styleUrls: ['./hogar.component.css']
})
export class HogarComponent implements OnInit {

  public productsArray:any = []

  constructor(private ProductService:ProductService) { }

  ngOnInit(): void {
    this.loadData();
  }

  public loadData(){
    this.ProductService.getProducts('https://stock-serviceutb.onrender.com/products/type?type=hogar')
    .subscribe(response =>{
      this.productsArray = response;
      console.log(response);
    })
  }

}
