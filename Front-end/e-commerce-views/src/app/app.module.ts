import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SelfProductComponent } from './components/self-product/self-product.component';

import { RouterModule } from '@angular/router';
import { NavbarComponent } from './components/navbar/navbar.component';
import { HomeComponent } from './components/home/home.component';
import { AboutComponent } from './components/about/about.component';
import { ProductsComponent } from './components/products/products.component';
import { LimpiezaComponent } from './components/limpieza/limpieza.component';
import { HogarComponent } from './components/hogar/hogar.component';
import { IndustrialComponent } from './components/industrial/industrial.component';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';
import { SettingsComponent } from './components/settings/settings.component';
import { CartComponent } from './components/cart/cart.component';
import { WishlistComponent } from './components/wishlist/wishlist.component';
import { ProvidersComponent } from './components/providers/providers.component';
import { AddProductComponent } from './components/add-product/add-product.component';
import { UpdateProductComponent } from './components/update-product/update-product.component';
import { HttpClientModule } from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';
import { ProductSearchComponent } from './components/product-search/product-search.component';

@NgModule({
  declarations: [
    AppComponent,
    SelfProductComponent,
    NavbarComponent,
    HomeComponent,
    AboutComponent,
    ProductsComponent,
    LimpiezaComponent,
    HogarComponent,
    IndustrialComponent,
    LoginComponent,
    RegisterComponent,
    SettingsComponent,
    CartComponent,
    WishlistComponent,
    ProvidersComponent,
    AddProductComponent,
    UpdateProductComponent,
    ProductSearchComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule,
    RouterModule.forRoot([
      {path:'', component:HomeComponent},
      {path:'product/:id', component:SelfProductComponent},
      {path:'about', component:AboutComponent},
      {path:'products', component:ProductsComponent},
      {path:'limpieza', component:LimpiezaComponent},
      {path:'hogar', component:HogarComponent},
      {path:'industrial', component:IndustrialComponent},
      {path:'carrito', component:CartComponent},
      {path:'wishlist', component:WishlistComponent},
      {path:'login', component:LoginComponent},
      {path:'registrarse', component:RegisterComponent},
      {path:'settings', component:SettingsComponent},
      {path:'login', redirectTo:'login', pathMatch:'full'},
      {path:'proovedores', component:ProvidersComponent},
      {path:'añadir', component:AddProductComponent},
      {path:'actualizar', component:UpdateProductComponent},
      {path: 'search/:name', component:ProductSearchComponent}
    ])
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
