describe('Testes de Pesquisa de Produtos', () => {
    it('pesquisa 1', () => {
        cy.visit('/produtos');

        cy.get(':nth-child(1) > .produtosCafe > .infoCafe > .imageCafe > .favorite > h2').then(($el) => { return $el.text() + " " ; }).as('Mocha');

        cy.get('#search').type('Mocha{enter}');

        cy.get('@Mocha').then((Mocha) => {
            cy.get('#nomeCafe').should('have.text', Mocha);
        })
    })

    it('pesquisa 2', () => {
        cy.visit('/produtos');

        cy.get(':nth-child(7) > .produtosCafe > .infoCafe > .imageCafe > .favorite > h2').then(($el) => { return $el.text() + " " ; }).as('cafePreto');

        cy.get('#search').type('Café Preto{enter}');

        cy.get('@cafePreto').then((cafePreto) => {
            cy.get('#nomeCafe').should('have.text', cafePreto);
        })
    })

    it('pesquisar café inexistente', () => {
        cy.visit('/produtos');

        cy.get('#search').type('Café Inexistente{enter}');

        cy.get('[style="color: red; font-size: 24px; text-align: center; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);"]').should('exist');
   }) 
})