import { Component, OnInit } from '@angular/core';
import { ProductService } from 'src/app/product.service';

@Component({
  selector: 'app-industrial',
  templateUrl: './industrial.component.html',
  styleUrls: ['./industrial.component.css']
})
export class IndustrialComponent implements OnInit {

  public productsArray:any = []

  constructor(private ProductService:ProductService) { }

  ngOnInit(): void {
    this.loadData();
  }

  public loadData(){
    this.ProductService.getProducts('https://stock-serviceutb.onrender.com/products/type?type=industrial')
    .subscribe(response =>{
      this.productsArray = response;
      console.log(response);
    })
  }

}
