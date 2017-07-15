import { SensitPage } from './app.po';

describe('sensit App', () => {
  let page: SensitPage;

  beforeEach(() => {
    page = new SensitPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!');
  });
});
