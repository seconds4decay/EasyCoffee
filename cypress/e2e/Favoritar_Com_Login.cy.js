describe('Testes de Favoritar', () => {
    let name = 'teste';
    let email = 'teste@cesar.school';
    let senha = '123';


    beforeEach(() => {
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

        cy.visit('/');
        cy.get('#login').click();
        cy.get('#nome').type(name);
        cy.get('#senha').type(senha);

        cy.on('uncaught:exception', (err, runnable) => {
            return false
        })

        cy.get('#login').click();
    })

    it('favoritar café', () => {
        cy.visit('/');
        cy.get('.square-main > :nth-child(1) > .square').click();

        cy.get(':nth-child(1) > .produtosCafe > .infoCafe > .imageCafe > .favorite > .nomeCafe').invoke('text').as('Mocha');

        cy.get(':nth-child(1) > .produtosCafe > .infoCafe > .imageCafe > .favorite > form > #favoritar-btn > .fas').click();
        cy.visit('/');
        cy.get('.hamburger-menu > .fa-solid').click();
        cy.get('[href="/favoritos"]').click();

        cy.get('@Mocha').then((Mocha) => {
            cy.get('.nomeCafe').should('have.text', Mocha);
        })
    })

    it('tirar café dos favoritos através da página de favoritos', () => {
        cy.visit('/');
        cy.get('.square-main > :nth-child(1) > .square').click();
        cy.get(':nth-child(1) > .produtosCafe > .infoCafe > .imageCafe > .favorite > form > #favoritar-btn > .fas').click();
        cy.visit('/');
        cy.get('.hamburger-menu > .fa-solid').click();
        cy.get('[href="/favoritos"]').click();
        cy.get('#favoritado').click();

        cy.get('.products').should('be.hidden');

        cy.visit('/');
        cy.get('.square-main > :nth-child(1) > .square').click();
        cy.get(':nth-child(1) > .produtosCafe > .infoCafe > .imageCafe > .favorite > form > #favoritar-btn > .fas').click();
    })

    it('tirar café dos favoritos através da página de produtos', () => {
        cy.visit('/');
        cy.get('.square-main > :nth-child(1) > .square').click();
        cy.get(':nth-child(1) > .produtosCafe > .infoCafe > .imageCafe > .favorite > form > #favoritar-btn > .fas').click();
        cy.get(':nth-child(1) > .produtosCafe > .infoCafe > .imageCafe > .favorite > form > #favoritar-btn > .fas').click();
        cy.visit('/');
        cy.get('.hamburger-menu > .fa-solid').click();
        cy.get('[href="/favoritos"]').click();

        cy.get('.products').should('be.hidden');

        cy.visit('/');
        cy.get('.square-main > :nth-child(1) > .square').click();
        cy.get(':nth-child(1) > .produtosCafe > .infoCafe > .imageCafe > .favorite > form > #favoritar-btn > .fas').click();
    })

    afterEach(() => {
        cy.visit('/');
        cy.get('.hamburger-menu > .fa-solid').click();
        cy.get('[href="/favoritos"]').click();
        cy.get('#favoritado').click();
        cy.visit('/');
        cy.get('#login').click();
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