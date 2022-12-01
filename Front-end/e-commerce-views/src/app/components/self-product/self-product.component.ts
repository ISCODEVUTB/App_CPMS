import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ProductService } from 'src/app/product.service';

@Component({
  selector: 'app-self-product',
  templateUrl: './self-product.component.html',
  styleUrls: ['./self-product.component.css']
})
export class SelfProductComponent implements OnInit {


  public productsArray:any = []

  id_prod: number = 0;

  onNotified(id:any){
    this.id_prod = id;
    console.log(this.id_prod);
  }

  constructor(private activatedRoute: ActivatedRoute, private service:ProductService) { }

  ngOnInit(): void {
    this.id_prod = Number(this.activatedRoute.snapshot.paramMap.get('id'));
    this.loadData(this.id_prod);
  }

  public loadData(id:number){
    this.service.getProducts('https://stock-serviceutb.onrender.com/products/active/'+this.id_prod)
    .subscribe(response =>{
      this.productsArray = response;
    })
  }


}
