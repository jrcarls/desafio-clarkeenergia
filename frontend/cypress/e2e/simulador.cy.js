describe("Simulador Clarke Energia", () => {
  beforeEach(() => {
    cy.visit("/");
  });

  it("deve carregar a página inicial", () => {
    cy.contains("Estado (UF)").should("be.visible");
    cy.contains("Consumo Mensal (kWh)").should("be.visible");
  });

  it("deve mostrar erro ao buscar sem preencher campos", () => {
    cy.contains("button", "Simular Economia").click();
    cy.contains("Por favor, selecione um estado e informe o consumo").should(
      "be.visible",
    );
  });

  it("deve abrir o autocomplete de estados", () => {
    cy.contains("Selecione um estado").click();
    cy.wait(1000);
  });

  it("deve realizar simulação com sucesso", () => {
    // Abre o autocomplete e seleciona um estado
    cy.contains("Selecione um estado").click();
    cy.wait(1000);
    // Aguarda carregar os estados da API e clica no primeiro
    cy.contains("SP", { timeout: 10000 }).first().click();

    // Preenche o consumo - clica no input do NumberFiel
    cy.contains("Consumo Mensal (kWh)").type("{selectall}500.0");

    cy.wait(1000);

    // Clica em simular
    cy.contains("Simular Economia").click();
  });
});
