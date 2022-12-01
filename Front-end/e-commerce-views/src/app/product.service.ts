import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Product } from './product';

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  constructor(private http: HttpClient) { }

  public getProducts(url:string):Observable<Product[]>{
    return this.http.get<Product[]>(url); //GET https://stock-serviceutb.onrender.com/products
  }

  public post(url:string, body:any){
    return this.http.post(url, body);
  }
}
