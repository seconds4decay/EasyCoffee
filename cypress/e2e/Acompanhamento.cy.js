describe('Acompanhamento para o Café', () => {
    
    it('visualizar lista de acompanhamentos', () => {
        cy.visit('/');
        cy.get('.hamburger-menu > .fa-solid').click();
        cy.get('[href="/acompanhamentos"]').click();

        cy.get('.glossary > :nth-child(1)').should('be.visible');
        cy.get(':nth-child(1) > .word').should('be.visible');
        cy.get(':nth-child(1) > .definition').should('be.visible');

    })

})