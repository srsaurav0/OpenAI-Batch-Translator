def get_text_lists():
    # Multiple lists of strings to translate
    texts_list_1 = get_inis()

    texts_list_2 = get_tpls()

    texts_list_3 = get_complex_sentences()

    texts_lists = [texts_list_1, texts_list_2, texts_list_3]

    return texts_lists

def get_inis():
    inis = [
        """RentByOwner.com offers a comprehensive online platform for travelers seeking the perfect vacation rental experience. With a wide selection of properties ranging from cozy holiday homes to luxurious villas, we cater to diverse travel needs and budgets. Our user-friendly website provides detailed property descriptions, photos, reviews, and easy booking options, ensuring a seamless rental process. RentByOwner.com aggregates over 10M properties from many travel sellers to give you a diverse selection of vacation homes to choose to create better travel memories.""",
        """<p> At Rent By Owner, we want everyone to be an owner, just as we want everyone to be a traveler. In creating more travelers, hopefully we are creating more owners. And in creating more owners, we will be creating more travelers. You can <a class="static-page-link" target="_blank" rel="noopener noreferrer" href="https://www.upnextgroup.com/about-us">read more about our core values</a> for UpNext Group here. We also look forward to showing you what we are creating in the months and years ahead. Stay tuned.</p>""",
        """<p> Historically, Rent By Owner has been a meta brand, connecting travelers to travel sellers, and since 2013, this has served us well. We believe that by helping more than a million travelers, we now have a great base on which to build something new and spectacular. Going forward, we need to build closer relationships with both sides of the market--both travelers and owners-- so as to bring them together in new ways and into a deeper relationship with each other and the communities into which the traveler journeys.</p>""",
        """<p> At Rent By Owner, we are focusing on the Alternative Accommodations market. We believe this market encourages people to have a more authentic travel experience in the communities, homes, and places of others. Creating a direct connection between a traveler and an owner creates a more meaningful experience. Sharing cultures, recipes, local tips, insights, pride, activities, art, food, entertainment... sights, sounds, smells and senses. These are the memories worth sharing.</p>""",
        """<p> We believe life is better when you venture out and explore the world. You meet other people, you connect with family & friends, you do more business, and you have new experiences. In short, travel creates memories. Travel brings people closer together and fosters better understanding of each other and ourselves.</p>""",
        """<p> Rent By Owner relies on the eco-score created by <a class="static-page-link" target="_blank" rel="noopener noreferrer" href="https://www.onedegreeleft.com">One Degree Left</a>, a sister-company operated by parent company UpNext Group. This property looks at a number of factors to help score all properties based on a variety of sustainability factors. We believe that we can help elevate properties that have good environmental and sustainability practices. If we identify a property that has good practices, we will rank that property higher in our search results than other properties. By ranking these properties higher, hopefully they will be booked with greater frequency and nudge behavior by a small factor… by ‘one degree’ if you will. While it is not perfect, it is part of our commitment to driving more sustainable travel.</p>"""
    ]
    return inis

def get_tpls():
    tpls = [
"""{{template "common/redirect/redirect.tpl" .}}

{{define "site_common_preload"}}
    <link rel="preload" href="{{.staticFileUrl}}/static/fonts/Muli_Webfont.woff2" as="font" type="font/woff2" crossorigin>
{{end}}

{{define "site_css"}}
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/redirect.css"/>
{{end}}

{{define "site_preload"}}
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/redirect.css" as="style"/>
{{end}}

{{define "site_header_logo_redirect"}}
    <a href="/" class="align-item-center">
        <img src="{{.staticFileUrl}}/static/images/sites/rentbyowner.com/header_logo.svg" alt="{{i18n .Lang "brand"}}" width="182" height="26">
    </a>
{{end}}

{{define "site_redirect_container_logo"}}
    <div class="box logo-area">
        <img src="{{.staticFileUrl}}/static/images/sites/rentbyowner.com/logo_footer.svg" alt="{{i18n .Lang "brand"}}" width="182" height="26" />
    </div>
{{end}}""",
"""{{template "sites/rentbyowner.com/layouts/main.tpl" .}}
{{template "common/details/published_details.tpl" .}}

{{define  "site_css_vars"}}
    <style>
        :root {
            /* Site 'Details' css image variable start*/
            --site-common-details-bottom-links-bullet: url({{.staticFileUrl}}/static/images/sites/rentbyowner.com/check.svg);
        }
    </style>
{{end}}

{{define "site_css"}}
    <link rel="stylesheet" type="text/css"
          href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css"/>
    <link rel="stylesheet" type="text/css"
          href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css"/>
    <link rel="stylesheet" type="text/css"
          href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/calendar.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/tiles.css"/>
    <link rel="stylesheet" type="text/css"
          href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/details.css"/>
{{end}}

{{define "site_preload"}}
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css"
          as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css"
          as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/calendar.css"
          as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/tiles.css"
          as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/details.css"
          as="style"/>
{{end}}

{{define "site_details_popup_header"}}
    <img class="max-w-full nav-row-logo" loading="lazy"
         src="{{.staticFileUrl}}/static/images/sites/rentbyowner.com/header_logo.svg" alt="{{i18n .Lang "brand"}}"
         width="182"
         height="26">
{{end}}

{{define "details_breadcrumb"}}
    {{template "common/details/partials/details_breadcrumb.tpl" .}}
{{end}}

{{define "map_area_description"}}
    {{template "common/details/partials/details_area_description_map.tpl" .}}
{{end}}

{{define "seo_room_arragment_faq"}}
    {{template "common/details/partials/details_seo_room_arragment_faq.tpl" .}}
{{end}}

{{define "map"}}
    {{template "common/details/partials/details_map.tpl" .}}
{{end}}

{{define "details_faq"}}
    {{template "common/details/partials/faq.tpl" .}}
{{end}}

{{define "details_mobile_review"}}
    {{template "common/details/partials/details_mobile_reviews.tpl" .}}
{{end}}

<!-- Bedroom footer content start -->
{{define "site_bedroom_footer_content"}}
    <div class="bedroom-footer-content">
        <div class="bedroom-footer text-white" id="js-seo-block">
            <div class="max-container">
                <div class="container-fluid">
                    <h3 class="bedroom-footer-title font-20 no-margin pb-16 underlined-title">
                        Why is Rent By Owner {{.LocationName}} Your Choice for Vacation Rentals
                    </h3>
                    <div class="color-accent">
                        <p>Find your dream vacation rental on Rent By Owner, where
                            adventure meets comfort in every corner. RentByOwner features a broad mix of accommodations,
                            from charming country cottages and chic city apartments to tranquil beachfront villas and
                            cozy mountain cabins. Whether you're yearning for a delightful bungalow by the bay, a grand
                            estate over the dock, or a snug lodge in a quaint village, we've got the perfect spot for
                            you.</p>
                        <div class="{{if eq .UserInfo.Platform "mobile"}}hidden{{else}}visible{{end}}" id="js-seo-text-section">
                            <p>Prepare to unleash your inner explorer with our unique lodgings, including floating
                                houses, whimsical treehouses, and picturesque farmhouses, or stick to the classics with
                                duplexes, flats, and guesthouses. Choose the simplicity of a studio or the luxury of a
                                suite. For outdoor enthusiasts, we offer tents in hidden campsites, RVs, mountain
                                cabins, boat rentals, chalets in snowy havens, and caravans in lush gardens. Rent By
                                Owner truly has something for everyone.</p>
                            <p>Every holiday rental, from a humble hut to a lavish resort, guarantees a memorable stay
                                with cozy beds, functional kitchens, and welcoming living areas. Ideal for families,
                                couples, or solo adventurers, our rentals are more than just a place to sleep—they're
                                your home away from home. Book your next vacation with us and embark on a unique retreat
                                crafted for relaxation and adventure. We also offer annexes for added privacy, designer
                                lofts for a modern touch, and motels for quick stays. Explore beachside bungalows,
                                countryside ranches, and urban condos. Find your perfect getaway, whether it’s a quiet
                                den in the forest or a bustling inn by the island. At RentByOwner, our properties
                                include everything from houseboats and barns to court-style quarters and garden
                                retreats.</p>
                            <p>To make your booking experience even more convenient, we help you compare prices and
                                inventory so you can find and book your vacation rental on popular platforms like
                                Airbnb, Expedia, Vrbo (previously HomeAway), TripAdvisor (FlipKey), Booking.com, and
                                HomeToGo. We work with these trusted sites to offer you a seamless booking process,
                                ensuring that your perfect vacation rental is just a few clicks away.</p>
                        </div>
                    </div>
                    <div class="read-more-less {{if eq .UserInfo.Platform "mobile"}}visible{{else}}hidden{{end}}">
                        <div class="read-more cursor-pointer" id="js-seo-read-more">
                            <span class="text-white">{{i18n .Lang "__show_more"}}</span>
                            <svg class="icon text-white">
                                <use xlink:href="#chevron-down-solid"></use>
                            </svg>
                        </div>
                        <div class="read-less read-more-container cursor-pointer hidden" id="js-seo-read-less">
                            <span class="text-white">{{i18n .Lang "show_less"}}</span>
                            <svg class="icon text-white">
                                <use xlink:href="#chevron-down-solid"></use>
                            </svg>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
{{end}}
<!-- Bedroom footer content start -->
""",
"""{{define "site_css"}}
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/calendar.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/faq_container.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/tiles.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/refine.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/sub_location.css"/>
{{end}}

{{define "site_preload"}}
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/calendar.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/faq_container.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/tiles.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/refine.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/sub_location.css" as="style"/>
{{end}}""",
"""<p>There are <span>{{if .PrivatePoolCount}}{{.PrivatePoolCount}}{{end}}</span> vacation rentals with private pools near <span>{{.LocationName}}</span>. Top-rated RBO homes that have access to a swimming pool include:</p>""",
"""{{template "sites/rentbyowner.com/layouts/main.tpl" .}}
{{template "common/listing/refine.tpl" .}}
{{template "common/partials/blank_bookmark_mobile.tpl" .}}

{{define  "site_css_vars"}}
    <style>
        :root {
            /* Site 'Category' css image variable start*/
            --site-common-listing-bottom-links-bullet: url({{.staticFileUrl}}/static/images/sites/rentbyowner.com/check.svg);
        }
    </style>
{{end}}

{{define "site_css"}}
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/calendar.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/tiles.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/category.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/refine.css"/>
{{end}}

{{define "site_preload"}}
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/calendar.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/tiles.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/category.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/refine.css" as="style"/>

{{end}}""",
"""{{template "sites/rentbyowner.com/layouts/main.tpl" .}}
{{template "common/listing/complex_list.tpl" .}}

{{define "site_css"}}
<link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css"/>
<link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css"/>
<link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/calendar.css"/>
<link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/tiles.css"/>
{{end}}

{{define "site_preload"}}
<link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css" as="style"/>
<link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css" as="style"/>
<link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/calendar.css" as="style"/>
<link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/tiles.css" as="style"/>
{{end}}
"""
    ]
    return tpls


def get_complex_sentences():
    sentences = [
        "Although the weather forecast predicted rain, we decided to go hiking, hoping the storm would pass quickly.",
        "The scientist, who had spent years studying marine life, discovered a new species of fish while conducting an expedition in the deep sea.",
        "After finishing her final exams, Sarah, exhausted but relieved, treated herself to a long weekend getaway with her friends.",
        "Despite the challenges of learning a new language, many students find that their ability to communicate improves rapidly with consistent practice.",
        "The book, which was recommended by my teacher, provided fascinating insights into the complexities of human behavior and decision-making.",
        "As the sun began to set, the sky turned a brilliant shade of pink, and we stood in awe, enjoying the quiet beauty of nature.",
        "While she was preparing dinner, her phone rang with an unexpected call, but she chose to ignore it in favor of finishing her task.",
        "The company, after years of growth and expansion, faced significant financial setbacks due to unforeseen market shifts and internal mismanagement.",
        "Although he was initially skeptical of the new technology, he soon realized its potential after attending the demonstration, which showcased its impressive capabilities.",
        "The concert, held in the heart of the city, attracted a diverse crowd, and the energy in the air was palpable as the band took the stage."
    ]
    return sentences