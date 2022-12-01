import { Component, OnInit } from '@angular/core';
import { ProductService } from 'src/app/product.service';

@Component({
  selector: 'app-limpieza',
  templateUrl: './limpieza.component.html',
  styleUrls: ['./limpieza.component.css']
})
export class LimpiezaComponent implements OnInit {

  public productsArray:any = []

  constructor(private ProductService:ProductService) { }

  ngOnInit(): void {
    this.loadData();
  }

  public loadData(){
    this.ProductService.getProducts('https://stock-serviceutb.onrender.com/products/type?type=limpieza')
    .subscribe(response =>{
      this.productsArray = response;
      console.log(response);
    })
  }

}
