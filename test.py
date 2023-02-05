def GetMidText(s, source = "https://towardsdatascience.com", preface = None):
    header = []
    all_text = []
    count = 0
    code = []
    ch6_list = []

    string_start_header =  '''<section data-bs-version="5.1" class="content4 cid-tt5SM2WLsM" id="content4-2" style="padding-top:0px; padding-bottom:0px; background-color: rgb(255, 255, 255);">
        <div class="container">
            <div class="row justify-content-center">
                <div class="title col-md-12 col-lg-10">
                    <h3 class="mbr-section-title mbr-fonts-style align-center mb-4 display-2">
                        <strong>'''
    string_end_header = '''
                </div>
            </div>
        </div>
    </section>'''
    string_start_article='''<section data-bs-version="5.1" class="content5 cid-tt5UseJ9wk" id="content5-4" style="padding-top:0px; padding-bottom:0px;background-color: rgb(255, 255, 255);">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-12 col-lg-9">'''

    string_end_article =  '''</div>
            </div>
        </div>
    </section>'''


    string_end_para = '''</div>
            </div>
        </div>
    </section>'''
    straing_start_figure = '''<section data-bs-version="5.1" class="gallery5 mbr-gallery cid-ttpUtpmN7q" id="gallery5-b">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-12 col-lg-9 item gallery-image">
                <div class="item-wrapper" data-toggle="modal" data-bs-toggle="modal" data-target="#ttpV27BHxB-modal" data-bs-target="#ttpV27BHxB-modal">'''

    string_start_figure = '''    <section data-bs-version="5.1" class="image3 cid-tt612oXwA9" id="image3-5" style="padding-top:0px; padding-bottom:0px; background-color: rgb(255, 255, 255);">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-12 col-lg-9">
                    <div class="image-wrapper">'''
    string_end_figure = '''</div>
                </div>
            </div>
        </div>
    </section>'''

    start_string_multi_figure ="""<section data-bs-version="5.1" class="gallery3 cid-ttaWMCQCls" id="gallery3-7" style="padding-top:0px; padding-bottom:0px; background-color: rgb(255, 255, 255);">
    
    
    <div class="container">"""
    start_string_multi_figure_item = '''
            <div class="item features-image сol-12 col-md-6 col-lg-6">
                <div class="item-wrapper">
                    <div class="item-img">'''
    end_string_multi_figure_item ='''                    </div>
                    
                    
                </div>
            </div>'''

    end_string_multi_figure ='''        </div>
    </div>
</section>
'''

    separator = '''    <section data-bs-version="5.1" class="content5 cid-tt5UseJ9wk" id="content5-4" style="padding-top:0px; padding-bottom:0px;background-color: rgb(255, 255, 255);">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-md-12 col-lg-10">
                <br>
                    <hr class="hr5">
                <br>
                </div>
            </div>
        </div>
    </section>'''
    all_text.append(string_start_article + '<br><br>' + preface + string_end_article)
    header_counter = 0
    for ch in s.children:
        #print(ch.name)
        for ch2 in ch:
            #print(ch2.name)
            for ch3 in ch2:
                if ch3.name == "section":
                    for ch4 in ch3:
                        for ch5 in ch4:
                            if ch5.name=="div":
                                try:
                                    if ch5['role'] == 'separator':
                                        all_text.append(separator)
                                except:
                                    pass
                                for ch6 in ch5:
                                    ########### Header ##############
                                    
                                    if ch6.name == "div":

                                        if header_counter == 0:
                                            for ch7 in ch6:

                                                if ch7.name =="h1":
                                                    #print(ch7.getText())
                                                
                                                    all_text.append(string_start_header  + ch7.getText().replace('<', '&lt;').replace('>', '&gt;') + '</h3>')
                                                    
                                                elif ch7.name =="h2" or ch7.name =="h3":
                                                    #print(ch7.getText())
                                                
                                                        all_text.append('<h4 class="mbr-section-subtitle align-center mbr-fonts-style mb-4 display-5">' + ch7.getText() + '</h4>')
                                                else:
                                                    tag = ch7.name
                                                    line ='<' + tag + '>' + ch7.getText().replace('<', '&lt;').replace('>', '&gt;') + '</' + tag+ '>'
                                                    all_text.append(line)
                                            all_text.append('<br>')
                                            all_text.append(string_end_header)
                                        
                                        elif header_counter > 0 :
                                            for ch7 in ch6:
                                                if ch7.name == "div":
                                                    img = ch7.find_all('picture')
                                                    ifr = ch7.find_all('iframe')
                                                    ala = ch7.find_all("a")
                                                    if not len(ifr) and not len(img):
                                                        all_text.append(string_start_article)
                                                        if len(ala):

                                                            src = ala[0]['href']
                                                            text = ch7.getText()
                                                            all_text.append(f'<a href="{src}">{text}</a>')
                                                        else:
                                                            all_text.append(ch7.getText())
                                                        all_text.append(string_end_article)
                                                    elif len(img):
                                                        for image in img:
                                                            all_text.append(string_start_figure)
                                                            src = image.find_all('source')[0]['srcset'].split()[-2]
                                                            all_text.append(f'<img src="{src}">' )
                                                            all_text.append(string_end_figure)
                                                    elif len(ifr):
                                                        for ifrs in ifr:
                                                            all_text.append(string_start_figure)
                                                            src = ifrs.extract()['src']
                                                                #idata = #GetfromIFrame(src)
                                                            pre_data = getPRE(src)
                                                            if pre_data:
                                                                idata = '<pre>' + pre_data + '</pre>'
                                                                all_text.append('<div class="iframe">' +idata +  '</div>')
                                                            all_text.append(string_end_figure)
                                                elif ch7.name == "a":
                                                    href = ch7.extract()['href']
                                                    if href.startswith('/'):
                                                        href = source+href
                                                
                                                    all_text.append(string_start_article)
                                                    all_text.append(f'<div class="sketchy"><a href="{href}">')
                                                
                                                    h2 = ch7.find('h2')
                                                    if h2.getText():
                                                        all_text.append('<h2 style="color:blueviolet; font-family:Arial, Helvetica, sans-serif; font-size:25px;">' + h2.getText() + '</h2>')
                                                    h3 = ch7.find('h3')
                                                    if h3.getText():
                                                        all_text.append('<h3 style="color:rgb(45, 34, 54); font-family:Arial, Helvetica, sans-serif; font-size:20px;">' + h3.getText() + '</h3>')
                                                    p = ch7.find('p')
                                                    if p.getText():
                                                        all_text.append('<p>' + p.getText() + '</p>')
                                                    all_text.append('<a></div>')
                                                    all_text.append(string_end_article)
                                                    all_text.append('<br>')

                                                        
                                        
                                        else:
                                            all_names = [ch7.name for ch7 in ch6]
                                            all_elem = [ch7 for ch7 in ch6]
                                            #print(all_names)
                                            if 'figure' in all_names:
                                                all_text.append(start_string_multi_figure)
                                                if all_names[0] != 'figure':
                                                    if all_elem[0].name == "h1" or all_elem[0].name == "h2" or all_elem[0].name == "h3":
                                                        text_add = ""
                                                        try:
                                                            for small in elem[0]:
                                                                if small.name == None:
                                                                    text_add += small.getText()
                                                                elif small.name == "a":
                                                                    src = small.extract()['href']
                                                                    text_add += f'<{small.name} href="{src}"> {small.getText()} </{small.name}>' 
                                                                else:
                                                                    text_add += f'<{small.name}> {small.getText()} </{small.name}>' 
                                                        except:
                                                            text_add = all_elem[0].getText()
                                                        

                                                        all_text.append(string_start_article)
                                                        all_text.append('<h4 class="mbr-section-subtitle align-center mbr-fonts-style mb-4 display-5">' + text_add.replace('<', '&lt;').replace('>', '&gt;') + '</h4>')
                                                        all_text.append(string_end_article)

                                                all_text.append('<div class="row mt-4">')


                                                for ch7 in ch6:
                                                    if ch7.name == 'figure':
                                                        for ch8 in ch7:
                                                            if ch8.name =="h1" or ch8.name =="h2" or ch8.name =="p" or ch8.name =="h3" or ch8.name =="h4":
                                                                fig_title = f'''<div class="mbr-section-head">
                                                                        <h5 class="mbr-section-subtitle mbr-fonts-style align-center mb-0 mt-2 display-5">{ch8.getText().replace('<', '&lt;').replace('>', '&gt;')}</h5>
                                                                        </div>'''
                                                                all_text.append(fig_title)
                                                        
                                                            elif ch8.name == 'picture':
                                                                all_text.append(start_string_multi_figure_item)
                                                                figure = ch8
                                                                src = list(figure.children)[0].get('srcset').split()[-2]
                                                                all_text.append('<img src =' + '"' + src + '">' )
                                                                all_text.append(end_string_multi_figure_item)
                                                            elif ch8.name == 'figcaption':
                                                                all_text.append('<p class="mbr-description mbr-fonts-style mt-2 align-center display-9">' + ch8.getText().replace('<', '&lt;').replace('>', '&gt;') + "</p>")
                                                            #all_text.append("<br>")
                                                all_text.append(end_string_multi_figure)

                                            else:
                                                if 'a' in all_names:
                                                    all_text.append(string_start_article)
                                                    for ch7 in ch6:
                                                        if ch7.name == 'a':
                                                            src = ch7.extract()['href']
                                                            all_text.append(f'<a href="{src}" target="_self">')
                                                            #for item in ch7:
                                                            #if item.name =="h2" or item.name =="h3" or item.name =="p":
                                                            all_text.append('<p>'+ src +'</p>')
                                                    all_text.append('</a>')
                                                    all_text.append(string_end_article)             

                                                
                                                    #all_text.append(f'<{ch7.name}>' + ch7.getText().replace('<', '&lt;').replace('>', '&gt;') + f'</{ch7.name}')
                                            #all_text.append(string_end_article)
                                            

                                        header_counter += 1
                                        
                                    
                                    ################ Text ##############
                                    elif ch6.name == "p":
                                        all_text.append(string_start_article)
                                        all_text.append('<p class="mbr-text mbr-fonts-style display-7">')
                                        #print(ch6.getText())
                                        for ch7 in ch6:
                                            #print(ch7.name)
                                            if ch7.name == None:
                                                #print(ch7.getText())
                                                all_text.append(ch7.getText().replace('<', '&lt;').replace('>', '&gt;'))
                                                #print(ch7.getText())
                
                                                #pass
                                            else:
                                                tag_name = ch7.name
                                                my_line = '<' + tag_name + ' >' + ch7.getText().replace('<', '&lt;').replace('>', '&gt;') + '</' + tag_name + '>'
                                                if tag_name == "a":
                                                    href = ch7['href']
                                                    if href[0] == "/":
                                                        href = source + href
                                                    my_line = '<' + tag_name + ' href=' + '"' + href +'"'' target="_self">' + ch7.getText().replace('<', '&lt;').replace('>', '&gt;') + '</' + tag_name + '>'
                                                all_text.append(my_line)
                                                
                                        all_text.append('</p>')
                                        all_text.append(string_end_article)



                                ################################  PRE
                                    elif ch6.name =="pre":
                                        for attr in ['data-selectable-paragraph', 'class', 'id']:
                                            for tag in ch6.find_all(attrs={attr: True}):
                                                del tag[attr]

                                        try:
                                            all_text.append(string_start_figure)
                                            all_text.append('</br>' + str(ch6) + '</br>')
                                            all_text.append(string_end_figure)
                                        except:
                                            print(ch6)
        
                                    ########## Figure parts ########################
                                    elif ch6.name == "figure":
                                        all_text.append(string_start_figure)

                                        for ch7 in ch6:
                                            #print(ch7.name)
                                            if ch7.name == "div":
                                                for ch8 in ch7:
                                                    #print(ch8.name) 
                                                    if ch8.name == "div":
                                                        
                                                        for ch9 in ch8:
                                                    
                                                            if ch9.name == 'picture':
                                                                figure = ch9
                                                                #print(list(figure.children)[0].get('srcset').split())
                                                                src = list(figure.children)[0].get('srcset').split()[-2]
                                                                all_text.append('<img src =' + '"' + src + '">' )
                                
                                                            elif ch9.name == 'iframe':
                                                                src = ch9.extract()['src']
                                                                #idata = #GetfromIFrame(src)
                                                                pre_data , flag = getPRE(src)
                                                                #print(src)
                                                                if flag :
                                                                    if pre_data:
                                                                        idata = '<pre>' + pre_data + '</pre>'
                                                                        all_text.append('<div class="iframe">' +idata +  '</div>' )
                                                                elif flag == False:
                                                                    all_text.append(f'<a href="{pre_data}">"Click Here!"</a>')
                                                    elif ch8.name == 'picture':
                                                        figure = ch8
                                                        src = list(figure.children)[0].get('srcset').split()[-2]
                                                        all_text.append('<img src =' + '"' + src + '">' )
                                  
                                            elif ch7.name == 'figcaption':
                                                all_text.append('<p class="mbr-description mbr-fonts-style mt-2 align-center display-9">' + ch7.getText().replace('<', '&lt;').replace('>', '&gt;') + "</p>")
                                            #all_text.append("<br>")
                                        all_text.append(string_end_figure)
                                        for ch7 in ch6:
                                            if ch7.name == "a":
                                                all_text.append('''<section data-bs-version="5.1" class="image3 cid-ttpo3s43l4" id="image3-9">
                                                <div class="container">
                                                    <div class="row justify-content-center">
                                                        <div class="col-12 col-lg-4">
                                                            <div class="image-wrapper">''')
                                                src = ch7.extract()['href']

                                                all_text.append(f'<a href="{src}">')
                                                src2 = ch7.find_all('picture')[0].find_all('source')[0]['srcset'].split()[-2]
                                                all_text.append('<img src =' + '"' + src2 + '">' )
                                                all_text.append('</a><br>')
                                                all_text.append('''</div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </section>''')
                                        

                                ################################ blockquote
                                    elif ch6.name == "blockquote":
                                        all_text.append('''<section data-bs-version="5.1" class="content7 cid-ttbhFZC4Ql" id="content7-8" style="padding-top:0px; padding-bottom:0px;background-color: rgb(255, 255, 255);">
    
                                        <div class="container">
                                            <div class="row justify-content-center">
                                                <div class="col-12 col-md-9">
                                                    <blockquote>
                                                                                        ''')
                                        for ch7 in ch6:
                                            if ch7.name == "p":
                                                all_text.append('<p class="mbr-text mbr-fonts-style display-5">')
                
                                                
                                                for ch8 in ch7:
                                                    #print(ch8.name)
                                                    if ch8.name == None:
                                                        all_text.append(ch8.getText().replace('<', '&lt;').replace('>', '&gt;'))

                                                    elif ch8.name == "strong":
                                                        all_text.append('<strong>' + ch8.getText().replace('<', '&lt;').replace('>', '&gt;') + '</strong>')
                                
                        
                                                    elif ch8.name == "a":
                                                        href = ch8.extract()['href']
                                                        if href[0] == "/":
                                                            href = source + href
                                                        all_text.append(f'<a href="{href}" target="_self">' + ch8.getText().replace('<', '&lt;').replace('>', '&gt;') + '</a>')
                         
                                                    elif ch8.name == "br":
                                                        all_text.append('<br/>')
                                                    elif ch8.name =="div":
                                                        print(ch8.getText())
                        
                                                    else:
                                                        all_text.append(ch8.getText().replace('<', '&lt;').replace('>', '&gt;'))
                        
                                                all_text.append("</p>")
                
                                        all_text.append('''</div></div></section>''')

                                #################################### unordered listed

                                    elif ch6.name == "ul":
                                        all_text.append(string_start_article)
                                        all_text.append("<ul>")
        
                                        for ch7 in ch6:
                                            if ch7.name == "li":
                                                #all_text.append(ch7.getText())
                                            
                                                counter_unlisted = 0
                                                unlisted_strong_temp = []
                                                all_text.append('<li>')
                                                for ch8 in ch7:
                                                    if ch8.name == "a":
                                                        href = ch8.extract()['href']
                                                        if href[0] == "/":
                                                            href = source + href
                                                        all_text.append(f'<a href="{href}" target="_self">' + ch8.getText().replace('<', '&lt;').replace('>', '&gt;') + '</a>') 
                                                    #unlisted_strong_temp.append([count, counter_unlisted, ch8.name, ch8.getText()])
                                                    #counter_unlisted += 1
                                                    elif ch8.name:
                                                        tag = ch8.name
                                                        all_text.append(f'<{tag}>' + ch8.getText().replace('<', '&lt;').replace('>', '&gt;') + f'</{tag}>') 
                                                    elif ch8.name == None:

                                                        all_text.append(ch8.getText().replace('<', '&lt;').replace('>', '&gt;')) 
                                                    
                                                all_text.append('</li>')
                                                #all_text.append(listed_format(unlisted_strong_temp))
                            
                
                                        all_text.append("</ul></br>")
                                        all_text.append(string_end_article)



                                #################################### ordered listed

                                    elif ch6.name == "ol":
                                        all_text.append(string_start_article)
                                        all_text.append("<ol>")
    
                                        for ch7 in ch6:
                                            if ch7.name == "li":
                                                #all_text.append(ch7.getText())
                                            
                                                counter_unlisted = 0
                                                unlisted_strong_temp = []
                                                all_text.append('<li>')
                                                for ch8 in ch7:
                                                    if ch8.name == "a":
                                                        href = ch8.extract()['href']
                                                        if href[0] == "/":
                                                            href = source + href
                                                        all_text.append(f'<a href="{href}" target="_self">' + ch8.getText() + '</a>') 
                                                    #unlisted_strong_temp.append([count, counter_unlisted, ch8.name, ch8.getText()])
                                                    #counter_unlisted += 1
                                                    elif ch8.name:
                                                        tag = ch8.name
                                                        all_text.append(f'<{tag}>' + ch8.getText() + f'</{tag}>') 
                                                    elif ch8.name == None:

                                                        all_text.append(ch8.getText()) 
                                                    
                                                all_text.append('</li>')
 
                            
                
                                        all_text.append("</ol></br>")
                                        all_text.append(string_end_article)
        
                                                                                            
                                ###################################### span
                                    elif ch6.name == "span":
                                        if len(ch6.getText()):
                                            all_text.append(string_start_article)
                                            all_text.append(ch6.getText())
                                            all_text.append(string_end_article)
                                    elif ch6.name == "br":
                                        all_text.append(string_start_article)
                                        all_text.append('</br>')
                                        all_text.append(string_end_article)
                                    elif ch6.name == "h1" or ch6.name == "h2":
                                        all_text.append(string_start_article)
                                        all_text.append('<h4 class="mbr-section-subtitle  mbr-fonts-style mb-4 display-5">')
                                    
                                        
                                        elems = [ch7 for ch7 in ch6]
                                        for elem in elems:
                                            if elem.name == "a":
                                                src = elem.extract()['href']
                                                if src.startswith("/"):
                                                    src = source + src 
                                                all_text.append(f'<a href="{src}"> {elem.getText()} </a>')
                                            elif elem.name != None:
                                                all_text.append(f'<{elem.name}> {elem.getText()} </{elem.name}>')
                                            else:
                                                all_text.append(elem.getText())
                                            
            
                                        #print(ch6.getText())
                                        
                                        all_text.append('</h4>')
                                        all_text.append(string_end_article)

                                    elif ch6.name == "div":
                                        print("hi")
                                        for element in ch6:
                                            if element.name == "a":
                                                print("Hi up") 
                                                if element['rel'] == 'noopener follow':
                                                    print("Hi") 
                                        #print(ch6)
                                    
                                    else:
                                        if ch6.name:
                                            all_text.append(string_start_article)
                                            tag = ch6.name
                                            line ='<' + tag + ' >' + ch6.getText() + '</' + tag+ '>'
                                            all_text.append(line)
                                            all_text.append(string_end_article)
                                        else:
                                            all_text.append(string_start_article)
                                            all_text.append(ch6.getText())
                                            all_text.append(string_end_article)

    all_text.append(string_start_article + '<br><br>' + string_end_article)
    return all_text
