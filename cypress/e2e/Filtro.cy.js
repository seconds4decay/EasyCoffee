describe('Testes de Filtro', () => {
    let name = 'teste';
    let email = 'teste@cesar.school'
    let senha = '123';

    before(() => {
        cy.visit('/');
        cy.get('#login').click();
        cy.get('#cadastrar-btn').click();

        cy.get('#nome').type(name);
        cy.get('#email').type(email);
        cy.get('#senha').type(senha);

        cy.on('uncaught:exception', (err, runnable) => {
            return false
        });


        cy.get('#login').click();
    })

    beforeEach(() => {
        cy.visit('/');
        cy.get('#login').click();
        cy.get('#nome').type(name);
        cy.get('#senha').type(senha);

        cy.on('uncaught:exception', (err, runnable) => {
            return false
        })

        cy.get('#login').click();
    })

    it('filtrar por tamanho', () => {
        cy.visit('/produtos');

        cy.get(':nth-child(1) > .produtosCafe > .infoCafe > .imageCafe > .favorite > .nomeCafe').invoke('text').as('Mocha');

        cy.get('#closed-filter-btn').click();
        cy.get('[for="tamanho2"] > img').click();
        cy.get('#filtrar-btn > input').click();

        cy.get('@Mocha').then((Mocha) => {
            cy.get(':nth-child(1) > .produtosCafe > .infoCafe > .imageCafe > .favorite > .nomeCafe').should('have.text', Mocha);
        })
    })

    it('filtrar por intensidade', () => {
        cy.visit('/produtos');

        cy.get(':nth-child(1) > .produtosCafe > .infoCafe > .imageCafe > .favorite > .nomeCafe').invoke('text').as('Mocha');

        cy.get('#closed-filter-btn').click();
        cy.get('[for="intensidade1"] > img').click();
        cy.get('#filtrar-btn > input').click();

        cy.get('@Mocha').then((Mocha) => {
            cy.get(':nth-child(1) > .produtosCafe > .infoCafe > .imageCafe > .favorite > .nomeCafe').should('have.text', Mocha);
        })
    })

    it('filtrar por aroma', () => {
        cy.visit('/produtos');

        cy.get(':nth-child(1) > .produtosCafe > .infoCafe > .imageCafe > .favorite > .nomeCafe').invoke('text').as('Mocha');

        cy.get('#closed-filter-btn').click();
        cy.get('[for="aroma4"] > img').click();
        cy.get('#filtrar-btn > input').click();

        cy.get('@Mocha').then((Mocha) => {
            cy.get(':nth-child(1) > .produtosCafe > .infoCafe > .imageCafe > .favorite > .nomeCafe').should('have.text', Mocha);
        })
    })

    it('filtrar por tamanho e intensidade', () => {
        cy.visit('/produtos');

        cy.get(':nth-child(1) > .produtosCafe > .infoCafe > .imageCafe > .favorite > .nomeCafe').invoke('text').as('Mocha');

        cy.get('#closed-filter-btn').click();
        cy.get('[for="tamanho2"] > img').click();
        cy.get('[for="intensidade1"] > img').click();
        cy.get('#filtrar-btn > input').click();

        cy.get('@Mocha').then((Mocha) => {
            cy.get(':nth-child(1) > .produtosCafe > .infoCafe > .imageCafe > .favorite > .nomeCafe').should('have.text', Mocha);
        })
    })

    it('filtrar por intensidade e aroma', () => {
        cy.visit('/produtos');

        cy.get(':nth-child(1) > .produtosCafe > .infoCafe > .imageCafe > .favorite > .nomeCafe').invoke('text').as('Mocha');

        cy.get('#closed-filter-btn').click();
        cy.get('[for="intensidade1"] > img').click();
        cy.get('[for="aroma4"] > img').click();
        cy.get('#filtrar-btn > input').click();

        cy.get('@Mocha').then((Mocha) => {
            cy.get(':nth-child(1) > .produtosCafe > .infoCafe > .imageCafe > .favorite > .nomeCafe').should('have.text', Mocha);
        })
    })

    it('filtrar por tamanho e aroma', () => {
        cy.visit('/produtos');

        cy.get(':nth-child(1) > .produtosCafe > .infoCafe > .imageCafe > .favorite > .nomeCafe').invoke('text').as('Mocha');

        cy.get('#closed-filter-btn').click();
        cy.get('[for="tamanho2"] > img').click();
        cy.get('[for="aroma4"] > img').click();
        cy.get('#filtrar-btn > input').click();

        cy.get('@Mocha').then((Mocha) => {
            cy.get(':nth-child(1) > .produtosCafe > .infoCafe > .imageCafe > .favorite > .nomeCafe').should('have.text', Mocha);
        })
    })

    it('filtrar por tamanho, intensidade e aroma', () => {
        cy.visit('/produtos');

        cy.get(':nth-child(1) > .produtosCafe > .infoCafe > .imageCafe > .favorite > .nomeCafe').invoke('text').as('Mocha');

        cy.get('#closed-filter-btn').click();
        cy.get('[for="tamanho2"] > img').click();
        cy.get('[for="intensidade1"] > img').click();
        cy.get('[for="aroma4"] > img').click();
        cy.get('#filtrar-btn > input').click();

        cy.get('@Mocha').then((Mocha) => {
            cy.get(':nth-child(1) > .produtosCafe > .infoCafe > .imageCafe > .favorite > .nomeCafe').should('have.text', Mocha);
        })
    })

    afterEach(() => {
        cy.visit('/');
        cy.get('#login').click();
    })

    after(() => {
        cy.visit('/admin');
        cy.get('#id_username').type('admin');
        cy.get('#id_password').type('123');
        cy.get('.submit-row > input').click();
        cy.get('.model-user > th > a').click();
        cy.get('#searchbar').type(name);
        cy.get('#changelist-search > div > [type="submit"]').click();
        cy.get(':nth-child(1) > .action-checkbox > .action-select').click();
        cy.get('select').select('Remover usuários selecionados');
        cy.get('.button').click();
        cy.get('div > [type="submit"]').click();
    })
})