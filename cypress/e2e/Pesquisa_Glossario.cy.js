describe('Testes de Pesquisa no Glossário', () => {
    let search1 = "Arábica";
    let search2 = "Adstringente";

    it('pesquisa 1', () => {
        cy.visit('/');
        cy.get(':nth-child(2) > .square').click();
        cy.get('#id_palavra').type(search1);
        cy.get('#id_palavra').type('{enter}');
        cy.get('h2').should('have.text', search1);
    })

    it('pesquisa 2', () => {
        cy.visit('/');
        cy.get(':nth-child(2) > .square').click();
        cy.get('#id_palavra').type(search2);
        cy.get('#id_palavra').type('{enter}');
        cy.get('h2').should('have.text', search2);
    })

    it('pesquisa errada', () => {
        cy.visit('/');
        cy.get(':nth-child(2) > .square').click();
        cy.get('#id_palavra').type("caféquenãoexiste");
        cy.get('#id_palavra').type('{enter}');
        cy.get('[style="color: red; font-size: 24px; text-align: center; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);"]').should('be.visible');
    })
})