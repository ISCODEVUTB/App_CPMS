import { Component, OnInit } from '@angular/core';
import { ProductService } from 'src/app/product.service';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-add-product',
  templateUrl: './add-product.component.html',
  styleUrls: ['./add-product.component.css']
})
export class AddProductComponent implements OnInit {

  public form?: FormGroup;

  constructor(private productService: ProductService, private formBuilder: FormBuilder) { }

  ngOnInit(): void {

    this.form = this.formBuilder.group({
      Name:['', Validators.required],
      Desc:['', Validators.required],
      Type:['', Validators.required],
      Price:['', Validators.required],
      Quantity:['', Validators.required],
      Active:[, ]

    })
  }

  public sendData(){
    this.productService.post('https://stock-serviceutb.onrender.com/products/',this.form)
  }

}
