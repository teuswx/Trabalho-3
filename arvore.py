def arvore_decisao():
    
    equipe = input("Você gosta de trabalhar em equipe? (sim/não): ").strip().lower()

    if equipe == "sim":
        
        ar_livre = input("Prefere atividades ao ar livre? (sim/não): ").strip().lower()
        if ar_livre == "sim":
            print("Sugestão: Explore atividades como esportes coletivos ou jardinagem.")
        else:
            
            tecnologia = input("Se sente confortável trabalhando com tecnologia? (sim/não): ").strip().lower()
            if tecnologia == "sim":
                
                resolver_problemas = input("Gosta de resolver problemas complexos? (sim/não): ").strip().lower()
                if resolver_problemas == "sim":
                    print("Sugestão: Considere áreas como engenharia, ciência ou tecnologia.")
                else:
                    print("Sugestão: Explore carreiras em TI ou áreas administrativas.")
            else:
                
                habilidades_artisticas = input("Prefere usar habilidades artísticas? (sim/não): ").strip().lower()
                if habilidades_artisticas == "sim":
                    print("Sugestão: Considere carreiras em artes ou design.")
                else:
                    
                    comunicacao = input("Prefere atividades que envolvam comunicação? (sim/não): ").strip().lower()
                    if comunicacao == "sim":
                        print("Sugestão: Áreas como marketing, jornalismo ou ensino podem ser interessantes.")
                    else:
                        print("Sugestão: Considere hobbies criativos como música ou fotografia.")
    else:
        
        numeros = input("Gosta de lidar com números? (sim/não): ").strip().lower()
        if numeros == "sim":
            
            resolver_problemas = input("Gosta de resolver problemas complexos? (sim/não): ").strip().lower()
            if resolver_problemas == "sim":
                print("Sugestão: Áreas como engenharia, ciência de dados ou economia podem ser ideais.")
            else:
                print("Sugestão: Explore carreiras em finanças ou contabilidade.")
        else:
            
            cuidar_pessoas = input("Se interessa por cuidar de outras pessoas? (sim/não): ").strip().lower()
            if cuidar_pessoas == "sim":
                print("Sugestão: Áreas como enfermagem, psicologia ou assistência social podem ser adequadas.")
            else:
                
                desafios_fisicos = input("Gosta de desafios físicos? (sim/não): ").strip().lower()
                if desafios_fisicos == "sim":
                    print("Sugestão: Considere carreiras ou hobbies relacionados a esportes ou atividades ao ar livre.")
                else:
                    
                    ambientes_organizados = input("Prefere trabalhar em ambientes organizados? (sim/não): ").strip().lower()
                    if ambientes_organizados == "sim":
                        print("Sugestão: Explore áreas administrativas ou de planejamento.")
                    else:
                        print("Sugestão: Considere hobbies individuais como leitura, escrita ou programação.")

# Chama a função
arvore_decisao()
