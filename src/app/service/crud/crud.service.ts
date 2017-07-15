import { Injectable } from '@angular/core';

import { AngularFireDatabase, FirebaseListObservable } from 'angularfire2/database';

@Injectable()
export class CrudService {

  constructor(db: AngularFireDatabase) { }

}
