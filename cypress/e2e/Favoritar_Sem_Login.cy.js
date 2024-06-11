describe('Testes de Favoritar Sem Login', () => {
    
    it('tentar favoritar sem login', () => {
        cy.visit('/');
        cy.get('.square-main > :nth-child(1) > .square').click();

        cy.get(':nth-child(1) > .produtosCafe > .infoCafe > .imageCafe > .favorite > form > #favoritar-btn > .fa-regular').click();

        cy.get('.login-fields').should('be.visible');
        
    })

    it('tentar acessar página de favoritos sem login', () => {
        cy.visit('/');
        cy.get('.hamburger-menu > .fa-solid').click();
        cy.get('[href="/favoritos"]').click();
        
        cy.get('.login-fields').should('be.visible');
    })

    
})