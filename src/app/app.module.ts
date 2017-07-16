import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { ChartsModule } from 'ng2-charts';
import { AngularFireModule } from 'angularfire2';
import { AngularFireDatabaseModule } from 'angularfire2/database';

import { environment } from '../environments/environment';

import { AppComponent } from './app.component';
import { BsDropdownModule } from 'ngx-bootstrap/dropdown';
import { TabsModule } from 'ngx-bootstrap/tabs';
import { ProgressbarModule } from 'ngx-bootstrap/progressbar';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    BsDropdownModule.forRoot(),
    ChartsModule,
    TabsModule.forRoot(),
    AngularFireModule.initializeApp(environment.firebase),
    ProgressbarModule.forRoot()
  ],
  providers: [],
  bootstrap: [AppComponent]
})

export class AppModule{}
export class DemoTabsVerticalPillsComponent {}
