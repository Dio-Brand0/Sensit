import { Injectable } from '@angular/core';

import { AngularFireDatabase, FirebaseListObservable } from 'angularfire2/database';

@Injectable()
export class CrudService {

  public thermal_items: FirebaseListObservable<any>;
  public moisture_items: FirebaseListObservable<any>;
  public soil_items: FirebaseListObservable<any>;

  constructor(db: AngularFireDatabase) { }

}
