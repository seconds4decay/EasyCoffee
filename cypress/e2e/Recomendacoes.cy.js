describe('Recomendações para o Usuário', () => {
    
    it('visualizar lista de recomendações', () => {
        cy.visit('/');
        cy.get('.buttons-inside > :nth-child(1) > .square').click();

        cy.get('.glossary').should('be.visible');
        cy.get('.glossary > :nth-child(1)').should('be.visible');
        cy.get('.glossary > :nth-child(2) > p > strong').should('be.visible');

    })

})