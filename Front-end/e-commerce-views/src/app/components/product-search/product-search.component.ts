import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ProductService } from 'src/app/product.service';

@Component({
  selector: 'app-product-search',
  templateUrl: './product-search.component.html',
  styleUrls: ['./product-search.component.css']
})
export class ProductSearchComponent implements OnInit {

  public productsArray:any = []

  public name?: string = "";

  constructor(private ProductService:ProductService, private activatedRoute: ActivatedRoute) { }

  ngOnInit(): void {
    this.name = String(this.activatedRoute.snapshot.queryParamMap.get('name'));
    this.loadData();
  }

  public loadData(){
    this.ProductService.getProducts('https://stock-serviceutb.onrender.com/products/search?name='+this.name)
    .subscribe(response =>{
      this.productsArray = response;
      console.log(response);
    })
  }

  

}
